class IOrderRepository:
    def fetch_one_by(self, nid):
        """
        获取单条数据的方法,所有继承当前类的类必须实现(有)该方法
        :param nid:
        :return:
        """
        raise Exception('子类中必须实现该方法！')

class OrderRepository(IOrderRepository):
    def fetch_one_by(self, nid):
        print(nid)
        
obj = OrderRepository()
obj.fetch_one_by(1)