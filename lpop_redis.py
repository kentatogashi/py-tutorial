import redis

while r.llen('mylist') > 0:
    print('pop', r.lpop('mylist').decode(), ' from mylist')
