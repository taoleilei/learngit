# class IOrderRepository:
#     def fetch_one_by(self, nid):
#         """
#         获取单条数据的方法,所有继承当前类的类必须实现(有)该方法
#         :param nid:
#         :return:
#         """
#         raise Exception('子类中必须实现该方法！')

# class OrderRepository(IOrderRepository):
#     def fetch_one_by(self, nid):
#         print(nid)
        
# obj = OrderRepository()
# obj.fetch_one_by(1)
# import re
# pattern = re.compile(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?")
# # print(pattern)
# print(re.match(pattern, 'alex3741@163.com'))

kwargs = {'name': 'alex', 'job': 'it', 'age': 18}
# sql = """
#     INSERT INTO merchant (%s)
#     VALUES
#         (% s)
# """
# key_list, value_list = [], []
# for k, v in kwargs.items():
#     key_list.append(k)
#     value_list.append('%%(%s)s' % k)
# sql = sql % (','.join(key_list), ','.join(value_list))
# # cursor.execute(sql, kwargs)
# # self.db_conn.close()
# print(sql)
# print(sql %(kwargs))
# print(key_list, value_list)

# sql = """
#     UPDATE merchant
#     SET % s
#     WHERE
#         nid =% s
# """
# value_list = []
# for k, v in kwargs.items():
#     value_list.append('%s=%%(%s)s' %(k, k))
# sql = sql % (','.join(value_list), 666)
# print(sql)
# print(sql % kwargs)
# print(value_list)

print(kwargs.items())