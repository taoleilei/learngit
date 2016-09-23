#!/usr/bin/env python
# -*- coding:utf-8 -*-
from ..Core.HttpRequest import WebRequestHandler
from Model.Category import CategoryService as ModelCategoryService
from Repository.CategoryRepository import CategoryRepository
from Service.Category.Service import CategoryService

from Model.Product import ProductService as ModelProductService
from Repository.ProductRepository import ProductRepository
from Service.Product.Service import ProductService
import json

from Mapper import Mapper

class IndexHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        # 依赖注入
        Mapper.register(ModelCategoryService, CategoryRepository())
        Mapper.register(CategoryService, ModelCategoryService())
        category_service = CategoryService()
        # 获取一级分类
        # 循环一级分类，获取二级分类
        # 循环二级分类，获取三级分类
        # c = CategoryService(CategoryRepository())
        category_list = category_service.get_all_category()
        # print(category_list)

        # 依赖注入
        Mapper.register(ModelProductService, ProductRepository())
        Mapper.register(ProductService, ModelProductService())
        product_service = ProductService()
        # p = ProductService(ProductRepository())
        product_dict = product_service.fetch_index_product()
        # print(product_dict)
        self.render('Home/Index.html', category_list=category_list, product_dict=product_dict.rows)



class DetailHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        product_id = kwargs.get('product_id', None)
        price_id = kwargs.get('price_id', None)
        if not product_id or not price_id:
            self.redirect('/Index.html')
            return

        # 依赖注入
        Mapper.register(ModelProductService, ProductRepository())
        Mapper.register(ProductService, ModelProductService())
        product_service = ProductService()
        # 根据商品ID获取商品信息，商户信息，价格列表，图片
        # p = ProductService(ProductRepository())
        product_dict = product_service.fetch_product_detail(product_id, price_id)

        self.render('Home/Detail.html', product_dict=product_dict.rows)


from tornado import escape

class PayHandler(WebRequestHandler):
    def get(self, *args, **kwargs):
        self.render('Home/Pay.html')

    def post(self):
        # 依赖注入
        Mapper.register(ModelProductService, ProductRepository())
        Mapper.register(ProductService, ModelProductService())
        product_service = ProductService()

        jd_buy_cookie = self.get_cookie('jd_buy_list')
        buy_str = escape.url_unescape(jd_buy_cookie)
        buy_list = json.loads(buy_str)
        data_list = []
        for item in buy_list:
            print(item)
            temp = {}
            product_title = item['product_title']
            product_img = item['product_img']

            count = item['count']
            price_id = item['price_id']
            temp["count"] = count
            temp["price_id"] = price_id

            
            result = product_service.fetch_price_detail(int(price_id))
            
            data_list.append(temp)
        print(data_list)
        print(result)
        self.write(json.dumps(data_list))