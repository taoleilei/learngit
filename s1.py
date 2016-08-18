import memcache

conn = memcache.Client(['192.168.127.129:12000'], debug=True)
conn.set('k1', 666)
ret = conn.get('k1')

# 添加一条键值对，如果已经存在的 key，重复执行add操作异常
# conn.add('k1', 888)

# replace 修改某个key的值，如果key不存在，则异常
# conn.replace('k3', 'v3')

# 设置多个键值对，如果key不存在，则创建，如果key存在，则修改
# conn.set_multi({'k1': 'v1', 'k2': 'v2'})
# 获取多个键值对
# ret = conn.get_multi(['k1','k2'])

# 在Memcached中删除指定的一个键值对
# conn.delete('k1')
# ret = conn.get('k1')

# 在Memcached中删除指定的多个键值对
# conn.delete_multi(['k1', 'k2'])
# ret = conn.get_multi(['k1','k2'])

# 修改指定key的值，在该值 后面 追加内容
# conn.set('k4', 'v4')
# conn.append('k4', '+after')
# ret = conn.get('k4')

# 修改指定key的值，在该值 前面 插入内容
# conn.set('k5', 'v5')
# conn.prepend('k5', 'before+')
# ret = conn.get('k5')

# 自增，将Memcached中的某一个值增加 N （ N默认为1 ）
# conn.set('k6', 10)
# conn.incr('k6')
# ret = conn.get('k6')

# 自增5
# conn.incr('k6', 5)
# ret = conn.get('k6')

# 自减，将Memcached中的某一个值减少 N （ N默认为1 ）
# conn.set('k7', 10)
# conn.decr('k7')
# ret = conn.get('k7')

# 自减5
# conn.set('k8', 10)
# conn.decr('k8', 5)
# ret = conn.get('k8')

# conn.delete_multi(['k4', 'k5', 'k6', 'k7', 'k8'])
print(ret, type(ret))
