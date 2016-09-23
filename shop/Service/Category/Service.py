from Service.Category.Response import CategoryResponse
from Mapper import MyType
import time
import datetime
import json


class CategoryService(metaclass=MyType):
    """docstring for CategoryService"""

    def __init__(self, model_category_service):
        self.modelCategoryService = model_category_service

    def get_all_category(self):
        response = self.modelCategoryService.get_all_category()
        return response
