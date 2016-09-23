import abc
from Mapper import MyType

# 业务接口
class IRegionRepository(metaclass=abc.ABCMeta):
    """docstring for IRegionRepository"""
    @abc.abstractmethod
    def fetch_province(self):
        """
        查询所有的省份
        :param username: 主键ID
        :param password: 主键ID
        :return:
        """
    @abc.abstractmethod
    def fetch_province_by_page(self, start, offset):
        """
        根据页数查找省份
        :param username: 主键ID
        :param password: 主键ID
        :return:
        """
    @abc.abstractmethod
    def exist_province(self, caption):
        """
        检查省份是否已经存在
        :param nid:
        :return:
        """
    @abc.abstractmethod
    def add_province(self, caption):
        """
        添加省份
        :param user_type_nid:
        :return:
        """
    @abc.abstractmethod
    def delete_province(self, province_nid):
        """
        删除省份
        :param caption:
        :return:
        """
    @abc.abstractmethod
    def update_province(self, province_nid, replace):
        """
        修改省份
        :param province_nid:
        :return:
        """
    @abc.abstractmethod
    def fetch_province_count(self):
        """
        获取所有省份个数
        :param province_nid:
        :return:
        """
    @abc.abstractmethod
    def fetch_city_by_province(self, province_nid):
        """
        根据省份查找市
        :param:
        :return:
        """
    @abc.abstractmethod
    def fetch_city_by_page(self, start, offset):
        """
        根据页码查找市
        :param:
        :return:
        """
    @abc.abstractmethod
    def fetch_city_count(self):
        """
        获取所有市个数
        :param:
        :return:
        """
    @abc.abstractmethod
    def exist_city(self, province_nid, caption):
        """
        检查市是否已经存在
        :param:
        :return:
        """
    @abc.abstractmethod
    def add_city(self, province_nid, caption):
        """
        添加市
        :param:
        :return:
        """
    @abc.abstractmethod
    def delete_city(self, city_nid):
        """
        删除市
        :param:
        :return:
        """
    @abc.abstractmethod
    def update_city(self, nid, province_nid, replace):
        """
        更新市
        :param:
        :return:
        """
    @abc.abstractmethod
    def fetch_county_by_page(self, start, offset):
        """
        根据页码查找县区
        :param:
        :return:
        """
    @abc.abstractmethod
    def fetch_county_count(self):
        """
        获取所有县区的数
        :param:
        :return:
        """
    @abc.abstractmethod
    def exist_county(self, city_id, caption):
        """
        检查县区是否存在
        :param:
        :return:
        """
    @abc.abstractmethod
    def add_county(self, city_nid, caption):
        """
        添加县区
        :param:
        :return:
        """     
    @abc.abstractmethod
    def delete_county(self, county_nid):
        """
        删除县区
        :param:
        :return:
        """ 
    @abc.abstractmethod
    def update_county(self, nid, city_nid, replace):
        """
        更新县区
        :param:
        :return:
        """ 
    @abc.abstractmethod
    def fetch_county_by_city(self, city_id):
        """
        
        """

# 协调
class RegionService(metaclass=MyType):
    """docstring for RegionService"""
    def __init__(self, region_repository):
        self.regionRepository = region_repository
    
    def get_province_count(self):
        count = self.regionRepository.fetch_province_count()
        return count

    def get_province_by_page(self, start, offset):
        result = self.regionRepository.fetch_province_by_page(start, offset)
        return result

    def get_province(self):
        return self.regionRepository.fetch_province()

    def create_province(self, caption):
        exist = self.regionRepository.exist_province(caption)
        if not exist:
            self.regionRepository.add_province(caption)
            return True

    def modify_province(self, province_nid, replace):
        exist = self.regionRepository.exist_province(replace)
        if not exist:
            self.regionRepository.update_province(province_nid, replace)
            return True

    def delete_province(self, province_nid):
        rows = self.regionRepository.delete_province(province_nid) 
        return rows

    def get_city_by_province(self, province_nid):
        rows = self.regionRepository.fetch_city_by_province(province_nid)
        return rows

    def get_city_count(self):
        count = self.regionRepository.fetch_city_count()
        return count

    def get_city_by_page(self, start, offset):
        result = self.regionRepository.fetch_city_by_page(start, offset)
        return result

    def create_city(self, province_nid, caption):
        exist = self.regionRepository.exist_city(province_nid, caption)
        if not exist:
            self.regionRepository.add_city(province_nid, caption)
            return True

    def delete_city(self, city_nid):
        rows = self.regionRepository.delete_city(city_nid)
        return rows

    def modify_city(self, nid, province_nid, replace):
        exist = self.regionRepository.exist_city(province_nid, replace)
        if not exist:
            self.regionRepository.update_city(nid, province_nid, replace)
            return True

    def get_county_count(self):
        count = self.regionRepository.fetch_county_count()
        return count

    def get_county_by_page(self, start, offset):
        result = self.regionRepository.fetch_county_by_page(start, offset)
        return result

    def create_county(self, city_nid, caption):
        exist = self.regionRepository.exist_county(city_nid, caption)
        if not exist:
            self.regionRepository.add_county(city_nid, caption)
            return True

    def delete_county(self, county_nid):
        rows = self.regionRepository.delete_county(county_nid)
        return rows

    def modify_county(self, nid, city_nid, replace):
        exist = self.regionRepository.exist_county(city_nid, replace)
        if not exist:
            self.regionRepository.update_county(nid, city_nid, replace)
            return True

    def get_county_by_city(self, city_nid):
        result = self.regionRepository.fetch_county_by_city(city_nid)
        return result
