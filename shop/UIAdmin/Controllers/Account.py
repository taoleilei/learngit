from UIAdmin.Core.HttpRequest import AdminRequestHandler
from Service.User.Request import UserRequest
from Service.User.Service import UserService
from Model.User import UserService as ModelUserService
from Repository.UserRepository import UserRepository
from Mapper import Mapper
from Infrastructure.Core.JsonString import JsonCustomEncoder
from Infrastructure.Core.EmailPattern import pattern
import json
import re


class LoginHandler(AdminRequestHandler):

    def get(self):
        self.render('Account/Login.html')

    def post(self):
        post_data = self.get_argument('post_data', None)
        post_data_dict = json.loads(post_data)
        if self.session['CheckCode'].upper() == post_data_dict.get('checkcode').upper():
            user = post_data_dict.get('username', None)
            if re.match(pattern, user):
                email = user
                user = None
            else:
                email = None
            pwd = post_data_dict.get('password', None)
            # Service层
            user_request = UserRequest(
                username=user, email=email, password=pwd)
            Mapper.register(ModelUserService, UserRepository())
            Mapper.register(UserService, ModelUserService())
            user_service = UserService()  # 依赖注入Model(业务逻辑层)的对应‘协调’
            response = user_service.check_login(user_request)
            if response.status:
                self.session['is_login'] = True
            response_str = json.dumps(response.status, cls=JsonCustomEncoder)
            self.write(response_str)

        