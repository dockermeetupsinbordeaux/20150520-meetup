from flask import Flask
from redis.sentinel import Sentinel
import os
app = Flask(__name__)

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
redis_cluster = os.environ.get('REDISSENTINEL1_ENV_CLUSTER_NAME')
sentinel = Sentinel(sentinels)
redis = sentinel.master_for(redis_cluster)

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
