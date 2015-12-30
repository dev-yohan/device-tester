import time
import os
from rq import Queue
import redis
from util import count_words_at_url

#redis_conn = Redis()
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

redis_conn = redis.from_url(redis_url)

q = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
while True:
    job = q.enqueue(count_words_at_url, 'http://www.eltiempo.com')
    print job.result   # => None

    # Now, wait a while, until the worker is finished
    time.sleep(2)
    print job.result   # => 889