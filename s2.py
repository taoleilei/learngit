import redis

# 普通操作模式
# r = redis.Redis(host='192.168.127.129', port=6379)
# r.set('foo', 'Bar666')
# ret = r.get('foo').decode('utf-8')
# print(ret, type(ret))

# 连接池
pool = redis.ConnectionPool(host='192.168.127.129', port=6379)
r = redis.Redis(connection_pool=pool)
# r.set('k1', 'v1')
# ret = r.get('k1').decode('utf-8')

# 批量设置值
# r.mset(k2='v2', k3='v3')
# r.mset({'k2': 'v2', 'k3': 'v3'})

# 批量获取值
# ret = r.mget('k2', 'k3')
# ret = r.mget(['k2', 'k3'])
# print(ret, type(ret))

# 获取子序列（根据字节获取，非字符）
# r.set('k4','获取子序列')
# 返回name对应值的字节长度（一个汉字3个字节）
# num = r.strlen('k4')
# ret = r.getrange('k4', 0, 5).decode('utf-8')
# print(ret)

# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# r.setrange('k4', 6, '长度')
# ret = r.get('k4').decode('utf-8')
# print(ret)

# 获取name对应的值的二进制表示中的某位的值 （0或1）
# r.set('k5', 'foo')
# ret = r.getbit('k5', 0)
# print(ret)

# 对name对应值的二进制表示的位进行操作
# r.set('k6', 'foo')
# r.setbit('k6', 7, 1)
# ret = r.get('k6')
# print(ret)

'''
获取name对应的值的二进制表示中 1 的个数
'''
# r.set('k7', 'foo')
# ret = r.bitcount('k7')
# print(ret)

# r.delete(['k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7'])

'''
name对应的hash中设置一个键值对（不存在，则创建；否则，修改）
'''
# r.hset('alex', 'age', 18)
# ret = r.hget('alex', 'age').decode('utf-8')
# print(ret, type(ret))


'''
在name对应的hash中批量设置键值对
'''
# r.hmset('eric', {'age': 20, 'job': 'it'})
# ret = r.hmget('eric', ['age', 'job'])
# print(ret, type(ret))

''' 
获取eric对应hash的所有键值
'''
# print(r.hgetall('eric'))
'''
获取eric对应的hash中键值对的个数
'''    
# print(r.hlen('eric'))
'''
获取eric对应的hash中所有的key的值
'''
# print(r.hkeys('eric'))
# print(r.hvals('eric'))
# print(r.hexists('eric', 'hobby'))

'''
cursor1, data1 = r.hscan('eric', cursor=0, match=None, count=None)
print(cursor1, data1)
cursor2, data2 = r.hscan('eric', cursor=cursor1, match=None, count=None)
print(cursor2, data2)
'''

'''
for item in r.hscan_iter('eric'):
    print(item)
'''

'''
管道
'''
pipe = r.pipeline()
r.set('name', 'alex')
r.set('rain', 'sb')
pipe.execute()
