#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from UIAdmin.Controllers import Account

settings = {
    'template_path': 'Views',  # 模板路径的配置
    'cookie_secret': 'sdfgsdfg',  # cookie加密
}

# 路由映射，路由系统
application = tornado.web.Application([
    (r"/index/", Account.IndexHandler),
], **settings)

if __name__ == "__main__":
    # socket运行起来
    application.listen(8888)
    print('Server HTTP on port 8888...')
    tornado.ioloop.IOLoop.instance().start()
