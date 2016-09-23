#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import abc
from Mapper import MyType


# 1、模型


class VipType:
    """docstring for VipType"""
    __VIP_TYPE = (
        {'nid': 1, 'caption': '铜牌'},
        {'nid': 2, 'caption': '银牌'},
        {'nid': 3, 'caption': '金牌'},
        {'nid': 4, 'caption': '铂金'},
    )

    def __init__(self, nid):
        self.nid = nid

    @property
    def get_caption(self):
        caption = None
        for item in VipType.__VIP_TYPE:
            if item['nid'] == self.nid:
                caption = item['caption']
                break
        return caption


class UserType:
    """docstring for UserType"""
    __USER_TYPE = (
        {'nid': 1, 'caption': '普通用户'},
        {'nid': 2, 'caption': '商户'},
        {'nid': 3, 'caption': '管理员'},
    )

    def __init__(self, nid):
        self.nid = nid

    @property
    def get_caption(self):
        caption = None
        for item in UserType.__USER_TYPE:
            if item['nid'] == self.nid:
                caption = item['caption']
                break
        return caption


class User:
    """docstring for User"""

    def __init__(self, nid, username, email, last_login, user_type, vip_type):
        self.nid = nid
        self.username = username
        self.email = email
        self.last_login = last_login
        self.user_type = user_type
        self.vip_type = vip_type


# 2、接口


class IUserReository(metaclass=abc.ABCMeta):
    """docstring for IUserReository"""

    @abc.abstractmethod
    def fetch_one_by_user_pwd(self, username, password):
        """
        根据用户名密码获取模型对象
        :param username: 主键ID
        :param password: 主键ID
        :return:
        """

    @abc.abstractmethod
    def fetch_one_by_email_pwd(self, email, password):
        """
        根据邮箱密码获取模型对象
        """

    @abc.abstractmethod
    def update_last_login_by_nid(self, nid, current_date):
        """
        根据ID更新最新登陆时间
        """

    @abc.abstractmethod
    def fetch_all(self, user_type_nid):
        """
        获取指定类型的所有用户（普通用户或商户）
        """

    @abc.abstractmethod
    def fetch_user(self):
        """
        """

# 3、协调


class UserService(metaclass=MyType):
    """docstring for UserServer"""

    def __init__(self, user_repository):
        self.user_repository = user_repository

    # print('Model层', self.user_repository)

    def check_login(self, username=None, email=None, password=None):
        # print(username, email, password)
        if username:
            user_model = self.user_repository.fetch_one_by_user_pwd(
                username, password)
        else:
            user_model = self.user_repository.fetch_one_by_email_pwd(
                email, password)
        if user_model:
            current_date = datetime.datetime.now()
            self.user_repository.update_last_login_by_nid(
                user_model.nid, current_date)
        # print('user_model', user_model)
        return user_model

    def get_users(self, user_type_nid):
        # print('Model层', self.user_repository)
        user_model = self.user_repository.fetch_all(
            user_type_nid)  # 获取一个包含多个对象的列表
        # print('Model', user_model)
        return user_model

    def get_user_to_select(self):

        user_list = self.user_repository.fetch_user()

        return user_list
