#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .CacheSession import CacheSession
from .MemcacheSession import MemcacheSession
from .RedisSession import RedisSession
import Config

class SessionFactory:
    if Config.SESSION_TYPE == 'cache':
        __session = CacheSession()
    elif Config.SESSION_TYPE == 'redis':
        __session = RedisSession()
    elif Config.SESSION_TYPE == 'memcached':
        __session = MemcacheSession()
    else:
        raise Exception('该类型不存在！')


    @staticmethod
    def get_session():
        return SessionFactory.__session


    @staticmethod
    def set_session(session):
        SessionFactory.__session = session