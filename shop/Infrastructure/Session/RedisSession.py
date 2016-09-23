#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .BaseSession import BaseSession
import redis
import Config
import json
import time

# pool = redis.ConnectionPool(host='192.168.127.129', port=6379)
# 创建连接池
pool = redis.ConnectionPool(**Config.REDIS_CONNECT)
r = redis.Redis(connection_pool=pool)

class RedisSession(BaseSession):

    def __init__(self):
        self.handler = None
        self.random_str = None

    def initialize(self, handler, expires):
        self.handler = handler
        # 从客户端获取随机字符串
        client_random_str = handler.get_cookie(RedisSession.session_id, None)
        # 如果从客户端获取到了随机字符串并且Redis中存在该字符串的name值
        #（redis中Hash的存储形式，一个name值对应一个hash的键值对）
        if client_random_str and r.exists(client_random_str):
            self.random_str = client_random_str
        else:
            # 客户端没有随机字符串，生成一个随机字符串
            self.random_str = RedisSession.create_session_id()
            # 初始化一个hash存储
            r.hset(self.random_str, None, None)
        # 为某个redis的某个name设置超时时间
        r.expire(self.random_str, Config.SESSION_EXPIRES)

        expires_time = time.time() + expires
        # 对浏览器设置cookie和超时时间
        handler.set_cookie(RedisSession.session_id,
                           self.random_str, expires=expires_time)

    def __getitem__(self, key):
        result = r.hget(self.random_str, key)
        if result:
            ret_str = str(result, encoding='utf-8')
            try:
                result = json.loads(ret_str)
            except:
                result = ret_str
            return result
        else:
            return result

    def __setitem__(self, key, value):
        if type(value) == dict:
            r.hset(self.random_str, key, json.dumps(value))
        else:
            r.hset(self.random_str, key, value)

    def __delitem__(self, key):
        r.hdel(self.random_str, key)
