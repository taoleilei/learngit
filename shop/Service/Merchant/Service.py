from Service.Merchant.Response import MerchantResponse
from Mapper import MyType


class MerchantService(metaclass=MyType):
    """docstring for Merchant"""

    def __init__(self, model_merchant_service):
        self.modelMerchantService = model_merchant_service

    def get_merchant_count(self):
        response = MerchantResponse()
        try:
            count = self.modelMerchantService.get_merchant_count()
            response.rows = count
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_merchant_by_page(self, start, rows):
        response = MerchantResponse()
        try:
            rows = self.modelMerchantService.get_merchant_by_page(start, rows)
            response.rows = rows
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def get_merchant_detail_by_nid(self, nid):
        response = MerchantResponse()
        try:
            rows = self.modelMerchantService.get_merchant_detail_by_nid(nid)
            response.rows = rows
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def create_merchant(self, **kwargs):
        response = MerchantResponse()
        try:
            self.modelMerchantService.create_merchant(kwargs)
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def delete_merchant(self, nid):
        response = MerchantResponse()
        try:
            self.modelMerchantService.delete_merchant(nid)
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response

    def update_merchant(self, nid, **kwargs):
        response = MerchantResponse()
        try:
            self.modelMerchantService.update_merchant(nid, kwargs)
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response
