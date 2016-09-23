import abc
from Mapper import MyType

# 模型


# 业务接口
class IProductRepository(metaclass=abc.ABCMeta):
    """docstring for IProductRepository"""
    @abc.abstractmethod
    def fetch_page_by_merchant_id(self, merchant_id, start, rows):
        """查询所有商户的数量"""

    @abc.abstractmethod
    def fetch_count_by_merchant_id(self, merchant_id):
        """根据页码查询商户"""

    @abc.abstractmethod
    def exist_product_by_pid(self, product_id):
        """根据商户id查询商户的详细"""

    @abc.abstractmethod
    def fetch_product_by_pid(self, product_id):
        """添加商户"""

    @abc.abstractmethod
    def fetch_product_by_id(self, merchant_id, product_id):
        """根据商户id删除商户"""

    @abc.abstractmethod
    def add_product(self, product_dict, detail_list, img_list):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def fetch_price_by_product_id(self,merchant_id, product_id):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def add_price(self, price_dict):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def update_price(self, nid, price_dict):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def fetch_product_pv(self, product_id):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def fetch_product_uv(self, product_id):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def add_product_puv(self, product_id, ip, current_date, current_timestamp):
        """根据商户id修改该商户详细"""

    @abc.abstractmethod
    def fetch_super_new_product(self):
        """
        获取首页新品上市的数据
        """
    @abc.abstractmethod
    def fetch_super_excellent_product(self):
        """
        获取首页精品推荐数据
        """

    @abc.abstractmethod
    def fetch_limit_price_and_product(self, subsite_caption):
        """
        """

    @abc.abstractmethod
    def fetch_product_and_merchant(self, product_id):
        """
        """

    @abc.abstractmethod
    def fetch_price_list(self, product_id):
        """
        """

    @abc.abstractmethod
    def fetch_price_detail(self, price_id):
        """
        """

    @abc.abstractmethod
    def fetch_image_list(self, product_id):
        """
        """

    @abc.abstractmethod
    def fetch_detail_list(self, product_id):
        """
        """

    @abc.abstractmethod
    def fetch_comment_list(self, product_id):
        """
        """

    @abc.abstractmethod
    def fetch_comment_count(self, product_id, fine):
        """
        """


# 协调
class ProductService(metaclass=MyType):
    """docstring for RegionService"""

    def __init__(self, product_repository):
        self.ProductRepository = product_repository

    def get_page_by_merchant_id(self, merchant_id, start, rows):
        result = self.ProductRepository.fetch_page_by_merchant_id(merchant_id, start, rows)
        return result

    def get_count_by_merchant_id(self, merchant_id):
        result = self.ProductRepository.fetch_count_by_merchant_id(merchant_id)
        return result

    def get_product_by_id(self, merchant_id, product_id):
        result = self.ProductRepository.fetch_product_by_id(merchant_id, product_id)
        return result

    def create_product(self, product_dict, detail_list, img_list):
        self.ProductRepository.add_product(product_dict, detail_list, img_list)

    def get_price_by_product_id(self, merchant_id, product_id):
        result = self.ProductRepository.fetch_price_by_product_id(merchant_id, product_id)
        return result

    def get_product_detail(self, merchant_id, product_id):
        pass

    def create_price(self, input_dict):
        self.ProductRepository.add_price(input_dict)

    def update_price(self, nid, input_dict):
        self.ProductRepository.update_price(nid, input_dict)

    def get_product_pv(self, product_id):
        result = self.ProductRepository.fetch_product_pv(product_id)
        return result

    def get_product_uv(self, product_id):
        result = self.ProductRepository.fetch_product_uv(product_id)
        return result

    def exist_product_by_pid(self, product_id):
        count = self.ProductRepository.exist_product_by_pid(product_id)
        return count

    def create_product_puv(self, product_id, ip, current_date, current_timestamp):
        self.ProductRepository.add_product_puv(product_id, ip, current_date, current_timestamp)

    def fetch_super_new_product(self):
        result = self.ProductRepository.fetch_super_new_product()
        return result

    def fetch_super_excellent_product(self):
        result = self.ProductRepository.fetch_super_excellent_product()
        return result

    def fetch_limit_price_and_product(self, name):
        result = self.ProductRepository.fetch_limit_price_and_product(name)
        return result

    def fetch_product_and_merchant(self, product_id):
        result = self.ProductRepository.fetch_product_and_merchant(product_id)
        return result

    def fetch_price_detail(self, price_id):
        result = self.ProductRepository.fetch_price_detail(price_id)
        return result

    def fetch_price_list(self, product_id):
        result = self.ProductRepository.fetch_price_list(product_id)
        return result

    def fetch_image_list(self, product_id):
        result = self.ProductRepository.fetch_image_list(product_id)
        return result

    def fetch_detail_list(self, product_id):
        result = self.ProductRepository.fetch_detail_list(product_id)
        return result

    def fetch_comment_list(self, product_id):
        result = self.ProductRepository.fetch_comment_list(product_id)
        return result

    def fetch_comment_count(self, product_id, num):
        result = self.ProductRepository.fetch_comment_count(product_id, num)
        return result
