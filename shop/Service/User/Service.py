from Service.User.Response import UserResponse
from Service.User.ModelView import UserModelView
from Mapper import MyType


class UserService(metaclass=MyType):
    """docstring for UserService"""

    def __init__(self, model_user_service):
        self.modelUserService = model_user_service

    def check_login(self, user_request):
        response = UserResponse()
        # print(self.modelUserService)
        # print('Service层', user_request, user_request.username)

        try:
            model = self.modelUserService.check_login(
                user_request.username, user_request.email, user_request.password)
            # print('Service', model, model.username)
            if not model:
                raise Exception('用户名或密码错误')
            else:
                model_view = UserModelView(nid=model.nid,
                                           username=model.username,
                                           email=model.email,
                                           last_login=model.last_login,
                                           user_type_id=model.user_type.nid,
                                           user_type_caption=model.user_type,
                                           vip_type_id=model.vip_type.nid,
                                           vip_type_caption=model.vip_type
                                           )
                response.modelView = model_view
        except Exception as e:
            response.status = False
            response.message = str(e)

        return response

    def show_users(self, user_type_nid):
        response = UserResponse()

        # print(user_type_nid)
        # print(self.modelUserService)
        try:
            model = self.modelUserService.get_users(
                user_type_nid)  # 获取一个包含多个对象的列表
            if len(model):
                modelViews = []
                for item in model:
                    # 每个item是一个用户对象
                    model_view = UserModelView(nid=item.nid,
                                               username=item.username,
                                               email=item.email,
                                               last_login=item.last_login,
                                               user_type_id=item.user_type.nid,    # user_type是一个UserType对象实例，里面封装了当前用户的nid
                                               user_type_caption=item.user_type.get_caption,    # get_caption是UserType类中的一个属性方法
                                               vip_type_id=item.vip_type.nid,
                                               vip_type_caption=item.vip_type.get_caption
                                               )
                    modelViews.append(model_view)
                response.modelViews = modelViews    # 一个包含多个对象的列表
            else:
                raise Exception('没有改用户类型或用户类型错误！ ')
        except Exception as e:
            response.status = False
            response.message = str(e)

        return response
