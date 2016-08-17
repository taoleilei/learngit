import redis
 
r = redis.Redis(host='192.168.127.129', port=6379)
r.set('foo', 'Bar666')
print(r.get('foo'))
print(r.get('index'))
