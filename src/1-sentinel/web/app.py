from flask import Flask
from redis.sentinel import Sentinel
import os
app = Flask(__name__)
sentinel = Sentinel([('localhost', 26379)])
redis = sentinel.master_for('meetup')

@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! I have been seen %s times.' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
