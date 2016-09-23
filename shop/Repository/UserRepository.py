#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 4、实现业务接口
# 具体SQL语句，pymysql
from Model.User import IUserReository
from Model.User import User
from Model.User import UserType
from Model.User import VipType
from Repository.DbConnection import DbConnection


class UserRepository(IUserReository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_one_by_email_pwd(self, email, password):
        ret = None

        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from userinfo where email=%s and password=%s"""
        cursor.execute(sql, (email, password))
        db_result = cursor.fetchone()
        self.db_conn.close()
        # print(type(db_result), db_result)
        if db_result:
            ret = User(nid=db_result['nid'],
                       username=db_result['username'],
                       email=db_result['email'],
                       last_login=db_result['last_login'],
                       user_type=UserType(nid=db_result['user_type']),
                       vip_type=VipType(nid=db_result['vip'])
                       )
        return ret

    def fetch_one_by_user_pwd(self, username, password):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from userinfo where username=%s and password=%s"""
        cursor.execute(sql, (username, password))
        db_result = cursor.fetchone()
        self.db_conn.close()

        if db_result:
            ret = User(nid=db_result['nid'],
                       username=db_result['username'],
                       email=db_result['email'],
                       last_login=db_result['last_login'],
                       user_type=UserType(nid=db_result['user_type']),
                       vip_type=VipType(nid=db_result['vip'])
                       )
        return ret

    def update_last_login_by_nid(self, nid, current_date):
        cursor = self.db_conn.connect()
        sql = """update userinfo set last_login=%s where nid=%s"""
        cursor.execute(sql, (current_date, nid))
        self.db_conn.close()

    def fetch_all(self, user_type_nid):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from userinfo where user_type=%s"""
        cursor.execute(sql, (user_type_nid))
        db_result = cursor.fetchall()   # 返回列表嵌套字典
        self.db_conn.close()

        # print('db_result', db_result)
        if db_result:
            result_all = []
            for item in db_result:
                result_all.append(User(nid=item['nid'],
                                       username=item['username'],
                                       email=item['email'],
                                       last_login=item['last_login'],
                                       user_type=UserType(
                                           nid=item['user_type']),
                                       vip_type=VipType(nid=item['vip'])
                                       ))
            return result_all

    def fetch_user(self):
        cursor = self.db_conn.connect()
        sql = """select nid as value,username as text from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result
