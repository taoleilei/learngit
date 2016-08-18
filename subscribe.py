import redis

pool = redis.ConnectionPool(host='192.168.127.129', port=6379)
r = redis.Redis(connection_pool=pool)

pub = r.pubsub()
pub.subscribe('fm104.5')
pub.parse_response()

while True:
    msg = pub.parse_response()
    print(msg)