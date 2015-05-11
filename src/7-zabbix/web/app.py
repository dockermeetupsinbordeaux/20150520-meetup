from flask import Flask
from redis.sentinel import Sentinel, MasterNotFoundError
import os
from textwrap import dedent

def load_sentinel():
    sentinels = []
    i = 1
    # get sentinels (ip, port) from environment
    while True:
        sentinel_ip_key = 'REDISSENTINEL%i_1_PORT_26379_TCP_ADDR' % i
        if sentinel_ip_key in os.environ:
            sentinels.append((
                os.environ[sentinel_ip_key],
                int(os.environ['REDISSENTINEL%i_PORT_26379_TCP_PORT' % i])
            ))
            i += 1
        else:
            break        
    return Sentinel(sentinels)

app = Flask(__name__)
sentinel = load_sentinel()
cluster_name = os.environ.get('REDISSENTINEL1_ENV_CLUSTER_NAME')
redis = sentinel.master_for(cluster_name)

def retry(func, *args, **kwargs):
    for _ in range(3):
        try:
            return func(*args, **kwargs)
        except MasterNotFoundError:
            raise
        except Exception as e:
            app.logger.exception(dedent('''\
                Redis operation failed: %s
                Retrying with another master'''), e)
            redis = sentinel.master_for(cluster_name)

@app.route('/')
def hello():
    retry(redis.incr, 'hits')
    return 'Hello World! I have been seen %s times.' % retry(redis.get, 'hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
