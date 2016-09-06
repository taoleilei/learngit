import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 调用协调者
        self.write("Hello, world")