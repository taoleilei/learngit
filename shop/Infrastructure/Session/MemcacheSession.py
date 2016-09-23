#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .BaseSession import BaseSession
import memcache
import json
import Config
import time

# conn = memcache.Client(['192.168.127.129:12000'], debug=True, cache_cas=True)
conn = memcache.Client(Config.MEMCACHE_CONNECT, debug=True, cache_cas=True)

class MemcacheSession(BaseSession):

    def __init__(self):
        self.handler = None
        self.random_str = None

    def initialize(self, handler, expires):
        self.handler = handler
        # 从客户端获取随机字符串
        client_random_str = handler.get_cookie(
            MemcacheSession.session_id, None)
        # 如果从客户端获取到了随机字符串并且Memcache中存在该字符串的键
        if client_random_str and conn.get(client_random_str):
            self.random_str = client_random_str
        else:
            # 客户端没有随机字符串，生成一个随机字符串
            self.random_str = MemcacheSession.create_session_id()
            # 设置一个键值对，如果key不存在，则创建，如果key存在，则修改
            conn.set(self.random_str, json.dumps({}), expires)
        # get获取一个键值对
        conn.set(self.random_str, conn.get(self.random_str), expires)
        expires_time = time.time() + expires
        # 对浏览器设置cookie和超时时间
        handler.set_cookie(MemcacheSession.session_id,
                           self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret = conn.get(self.random_str)
        ret_dict = json.loads(ret)
        result = ret_dict.get(key, None)
        return result

    def __setitem__(self, key, value):
        ret = conn.get(self.random_str)
        ret_dict = json.loads(ret)
        ret_dict[key] = value
        conn.set(self.random_str, json.dumps(ret_dict), Config.SESSION_EXPIRES)

    def __delitem__(self, key):
        ret = conn.get(self.random_str)
        ret_dict = json.loads(ret)
        del ret_dict[key]
        conn.set(self.random_str, json.dumps(ret_dict), Config.SESSION_EXPIRES)
