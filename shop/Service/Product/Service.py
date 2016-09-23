from Service.Product.Response import ProductResponse
from Mapper import MyType
import time
import datetime
import json


class ProductService(metaclass=MyType):
    """docstring for Merchant"""

    def __init__(self, model_product_service):
        self.modelProductService = model_product_service


    def get_page_by_merchant_id(self, merchant_id, start, row):
        response = ProductResponse()
        try:
            count = self.modelProductService.get_count_by_merchant_id(merchant_id)
            result = self.modelProductService.get_page_by_merchant_id(merchant_id, start, row)
            response.rows = {'count': count, 'result': result}
        except Exception as e:
            response.success = False
            response.message = str(e)            
        return response

    def get_product_by_id(self, merchant_id, product_id):
        response = ProductResponse()
        try:
            result = self.modelProductService.get_product_by_id(merchant_id, product_id)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)         
        return result

    def create_product(self, merchant_id, input_dict):
        response = ProductResponse()
        try:
            product_dict = {
                'merchant_id': merchant_id,
                'title': input_dict['title'],
                'img': input_dict['img'],
                'category_id': 1,
                'ctime': time.strftime('%Y-%m-%d')
            }
            detail_list = json.loads(input_dict['detail_list'])
            img_list = json.loads(input_dict['img_list'])
            self.modelProductService.create_product(product_dict, detail_list, img_list)
        except Exception as e:
            response.success = False
            response.message = str(e)   
        return response

    def get_price_by_product_id(self, merchant_id, product_id):
        response = ProductResponse()
        try:
            result = self.modelProductService.get_price_by_product_id(merchant_id, product_id)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response

    def get_product_detail(self, merchant_id, product_id):
        response = ProductResponse()
        try:
            is_valid = self.modelProductService.get_product_detail(merchant_id, product_id)
            if not is_valid:
                response.success = False
                response.message = '商品不存在'
            else:
                pass
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response            


    def create_price(self, merchant_id, product_id, input_dict):
        response = ProductResponse()
        try:
            # 检查当前用户是否有权限为该商品增加规格
            is_valid = self.modelProductService.get_product_by_id(merchant_id, product_id)
            if not is_valid:
                response.success = False
                response.message = '无权创建规格'
            else:
                self.modelProductService.create_price(input_dict)
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response    
        

    def update_price(self, merchant_id, product_id, nid, input_dict):
        response = ProductResponse()
        try:
            # 检查当前用户是否有权限为该商品增加规格
            is_valid = self.modelProductService.get_product_by_id(merchant_id, product_id)
            if not is_valid:
                response.success = False
                response.message = '无权更新规格'
            else:
                self.modelProductService.update_price(nid, input_dict)
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response 


    def get_upv(self, merchant_id, product_id):
        response = ProductResponse()
        try:
            is_valid = self.modelProductService.get_product_by_id(merchant_id, product_id)
            if not is_valid:
                response.message = '无权获取PUV'
                response.success = False
            else:              
                pv = self.modelProductService.get_product_pv(product_id)
                uv = self.modelProductService.get_product_uv(product_id)
                response.rows = [{'name': 'pv', 'data': pv}, {'name': 'uv', 'data': uv}]
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response

    def create_puv(self, product_id, ip):
        response = ProductResponse()
        try:
            has_exist = self.modelProductService.exist_product_by_pid(product_id)
            if not has_exist:
                response.success = False
                response.message = '商品ID不存在'
            else:
                current_date = time.strftime('%Y-%m-%d')
                current_timestamp = time.mktime(datetime.datetime.strptime(current_date, "%Y-%m-%d").timetuple()) * 1000

                self.modelProductService.create_product_puv(product_id, ip, current_date, current_timestamp)
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response




    def fetch_index_product(self):
        response = ProductResponse()
        try:
            super_new_list = self.modelProductService.fetch_super_new_product()
            super_excellent_list = self.modelProductService.fetch_super_excellent_product()

            a = self.modelProductService.fetch_limit_price_and_product('家具城')
            b = self.modelProductService.fetch_limit_price_and_product('建材城')
            c = self.modelProductService.fetch_limit_price_and_product('家具家装')
            response.rows = {
                'super_new_list': super_new_list,
                'super_excellent_list': super_excellent_list,
                'furniture': a,
                'building_materials': b,
                'decoration': c
            }
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response

    def fetch_product_detail(self, product_id, price_id):
        response = ProductResponse()
        try:
            product_detail = self.modelProductService.fetch_product_and_merchant(product_id)
            price_detail = self.modelProductService.fetch_price_detail(price_id)
            price_list = self.modelProductService.fetch_price_list(product_id)

            image_list = self.modelProductService.fetch_image_list(product_id)
            detail_list = self.modelProductService.fetch_detail_list(product_id)
            comment_list = self.modelProductService.fetch_comment_list(product_id)

            fine = self.modelProductService.fetch_comment_count(product_id, 1)
            no_fine = self.modelProductService.fetch_comment_count(product_id, 2)

            response.rows = {
                'product_detail': product_detail,
                'price_detail': price_detail,
                'price_list': price_list,
                'image_list': image_list,
                'detail_list': detail_list,
                'comment_list': comment_list,
                'comment_count': {'fine': fine, 'fine_percent': fine/(fine+no_fine) * 100 if fine else 0, 'no_fine': no_fine, 'no_fine_percent': no_fine/(fine+no_fine)* 100 if no_fine else 0,'total': fine+no_fine}
            }
        except Exception as e:
            response.success = False
            response.message = str(e)  
        return response

    def fetch_price_detail(self, price_id):
        response = ProductResponse()
        try:
            result = self.modelProductService.fetch_price_detail(price_id)
            response.rows = result
        except Exception as e:
            response.success = False
            response.message = str(e)
        return response