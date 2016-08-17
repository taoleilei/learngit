import memcache

conn = memcache.Client(['192.168.127.129:12000'], debug=True)
conn.set_multi({'k1': 'v1', 'k2': 'v2'})
ret = conn.get_multi(['k1','k2'])
print(ret)
