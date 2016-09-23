from UIAdmin.Core.HttpRequest import AdminRequestHandler
from Service.Product.Service import ProductService
from Model.Product import ProductService as modelProductService
from Repository.ProductRepository import ProductRepository
from Mapper import Mapper
from UIAdmin.Forms.Product import JdProductForm
from UIAdmin.Forms.Product import JdProductPriceForm
import json
import datetime


class ProductManagerHandler(AdminRequestHandler):
    """docstring for ProductManagerHandler"""
    def get(self):
        self.render('Product/JdProductManager.html')


class JdProductHandler(AdminRequestHandler):
    """docstring for JdProductHandler"""
    def get(self):
        """
        根据参数，获取产品信息（type：自营（商户ID），type：所有商品）
        后台管理用户登陆成功后，Session中保存自营ID
        自营ID＝1
        """
        # 手动获取京东自营ID为14
        merchant_id = 14
        page = int(self.get_argument('page', 1))
        rows = int(self.get_argument('rows', 10))
        start = (page-1) * rows
        # 依赖注入
        Mapper.register(modelProductService, ProductRepository())
        Mapper.register(ProductService, modelProductService())
        product_service = ProductService()
        
        response = product_service.get_page_by_merchant_id(merchant_id, start, rows)