import redis

pool = redis.ConnectionPool(host='192.168.127.129', port=6379)
r = redis.Redis(connection_pool=pool)

r.publish('fm104.5', 666)