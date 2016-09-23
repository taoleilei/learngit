import abc
from Mapper import MyType

# 模型


# 业务接口
class IMerchantRepository(metaclass=abc.ABCMeta):
    """docstring for IMerchantRepository"""
    @abc.abstractmethod
    def fetch_merchant_count(self):
        """查询所有商户的数量"""

    @abc.abstractmethod
    def fetch_merchant_by_page(self, start, rows):
        """根据页码查询商户"""

    @abc.abstractmethod
    def fetch_merchant_detail_by_nid(self, nid):
        """根据商户id查询商户的详细"""

    @abc.abstractmethod
    def add_merchant(self, **kwargs):
        """添加商户"""

    @abc.abstractmethod
    def detete_merchant(self, nid):
        """根据商户id删除商户"""

    @abc.abstractmethod
    def update_merchant(self, nid, **kwargs):
        """根据商户id修改该商户详细"""


# 协调
class MerchantService(metaclass=MyType):
    """docstring for RegionService"""

    def __init__(self, merchant_repository):
        self.MerchantRepository = merchant_repository

    def get_merchant_count(self):
        count = self.MerchantRepository.fetch_merchant_count()
        return count

    def get_merchant_by_page(self, start, rows):
        result = self.MerchantRepository.fetch_merchant_by_page(start, rows)
        return result

    def get_merchant_detail_by_nid(self, nid):
        result = self.MerchantRepository.fetch_merchant_detail_by_nid(nid)
        return result

    def create_merchant(self, **kwargs):
        self.MerchantRepository.add_merchant(**kwargs)

    def delete_merchant(self, nid):
        self.MerchantRepository.detete_merchant(nid)

    def update_merchant(self, nid, **kwargs):
        self.MerchantRepository.update_merchant(**kwargs)
