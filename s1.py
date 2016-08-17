import memcache
 
mc = memcache.Client(['192.168.127.129:12000'], debug=True)
mc.set("foo", "bar")
ret = mc.get('foo')
print(ret)