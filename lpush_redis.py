import redis
import time

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    for i in range(1000):
        r.lpush('mylist', i)
        print('pushed ', i, ' to mylist')
        time.sleep(1)
