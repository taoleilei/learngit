from Service.Region.Response import RegionResponse
from Mapper import MyType


class RegionService(metaclass=MyType):
    """docstring for Region"""

    def __init__(self, model_region_service):
        self.modelRegionService = model_region_service

    def get_province_count(self):
        response = RegionResponse()
        try:
            count = self.modelRegionService.get_province_count()
            response.rows = count
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_province_by_page(self, start, offset):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_province_by_page(
                start, offset)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_province(self):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_province()
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def create_province(self, caption):
        response = RegionResponse()
        try:
            result = self.modelRegionService.create_province(caption)
            response.rows = result
            if not result:
                response.success = False
                response.message = '省份已经存在'
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def modify_province(self, province_nid, replace):
        response = RegionResponse()
        try:
            result = self.modelRegionService.modify_province(
                province_nid, replace)
            response.rows = result
            if not result:
                response.success = False
                response.message = '省份已经存在'
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def delete_province(self, province_nid):
        response = RegionResponse()
        try:
            result = self.modelRegionService.delete_province(province_nid)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_city_by_province(self, province_nid):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_city_by_province(province_nid)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_city_count(self):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_city_count()
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_city_by_page(self, start, offset):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_city_by_page(start, offset)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def create_city(self, province_nid, caption):
        response = RegionResponse()
        try:
            result = self.modelRegionService.create_city(province_nid, caption)
            response.rows = result
            if not result:
                response.success = False
                response.message = '市已经存在'
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def delete_city(self, city_nid):
        response = RegionResponse()
        try:
            result = self.modelRegionService.delete_city(city_nid)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def modify_city(self, nid, province_nid, replace):
        response = RegionResponse()
        try:
            result = self.modelRegionService.modify_city(
                nid, province_nid, replace)
            response.rows = result
            if not result:
                response.success = False
                response.message = '市已经存在'
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_county_count(self):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_county_count()
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_county_by_page(self, start, offset):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_county_by_page(start, offset)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def create_county(self, city_nid, caption):
        response = RegionResponse()
        try:
            result = self.modelRegionService.create_county(city_nid, caption)
            response.rows = result
            if not result:
                response.success = False
                response.message = '县（区）已经存在'
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def delete_county(self, county_nid):
        response = RegionResponse()
        try:
            result = self.modelRegionService.delete_county(county_nid)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def modify_county(self, nid, city_nid, replace):
        response = RegionResponse()
        try:
            result = self.modelRegionService.modify_county(
                nid, city_nid, replace)
            response.rows = result
            if not result:
                response.success = False
                response.message = '县（区）已经存在'
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_county_by_city(self, city_nid):
        response = RegionResponse()
        try:
            result = self.modelRegionService.get_county_by_city(city_nid)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

