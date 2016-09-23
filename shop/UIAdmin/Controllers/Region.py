from UIAdmin.Core.HttpRequest import AdminRequestHandler
from Service.Region.Service import RegionService
from Model.Region import RegionService as ModelRegionService
from Repository.RegionRepository import RegionRepository
from Mapper import Mapper
import json


class ProvinceManagerHandler(AdminRequestHandler):
    """docstring for ManageHandler"""

    def get(self):
        # 获取所有用户，商户的信息
        if self.session['is_login']:
            self.render('Account/ProvinceManager.html')
        else:
            self.redirect('/login.html')
        # self.render('Region/ProvinceManager.html')


class ProvinceHandler(AdminRequestHandler):
    """docstring for ManageHandler"""

    def get(self):
        """获取"""
        # 依赖注入
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()
        if self.get_argument('type', None) == 'all':
            response = region_service.get_province()
            # print(response.rows)
            # print(response.success)
            # print(response.message)
            ret = response.__dict__
        else:
            page = int(self.get_argument('page', 1))
            rows = int(self.get_argument('rows', 10))
            start = (page - 1) * rows
            rows_list = region_service.get_province_by_page(start, rows)
            rows_count = region_service.get_province_count()
            ret = {'total': rows_count.rows, 'rows': rows_list.rows}
        self.write(json.dumps(ret))

    def post(self):
        """添加"""
        # 依赖注入
        ret = {'success': False, 'message': ""}
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        caption = self.get_argument('caption', None)
        # print(caption)
        if not caption:
            ret['message'] = '输入不能为空'
        else:
            response = region_service.create_province(caption)
            ret = response.__dict__
        self.write(json.dumps(ret))

    def put(self):
        """修改数据"""
        ret = {'success': False, 'message': ""}
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        province_nid = self.get_argument('nid', None)
        replace = self.get_argument('caption', None)
        # print(province_nid,replace)
        if not replace or not province_nid:
            ret['message'] = '输入不能为空'
        else:
            response = region_service.modify_province(int(province_nid), replace)
            ret = response.__dict__
        self.write(json.dumps(ret))

    def delete(self):
        """删除数据"""
        ret = {'success': False, 'message': ""}
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        province_nid = self.get_argument('nid', None)
        # print(province_nid)
        if not province_nid:
            ret['message'] = '输入不能为空'
        else:
            response = region_service.delete_province(province_nid)
            # print(response.message)
            # print(response.success)
            # print(response.rows)
            ret = response.__dict__
        self.write(json.dumps(ret))


class CityManagerHandler(AdminRequestHandler):
    """docstring for CityManagerHandler"""

    def get(self):
        self.render('Region/CityManager.html')


class CityHandler(AdminRequestHandler):
    """docstring for CityHandler"""

    def get(self):
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}
        if self.get_argument('type', None) == 'province':
            province_nid = self.get_argument('province_id', None)
            # print(province_nid)
            if not province_nid:
                ret['message'] = '请指定省份ID'
            else:
                response = region_service.get_city_by_province(province_nid)
                ret = response.__dict__
        else:
            page = int(self.get_argument('page', 1))
            rows = int(self.get_argument('rows', 10))
            start = (page - 1) * rows

            rows_list = region_service.get_city_by_page(start, rows)
            rows_count = region_service.get_city_count()
            ret['success'] = all([rows_list.success, rows_count.success])
            ret['message'] = rows_list.message + rows_count.message
            ret.update({'total': rows_count.rows, 'rows': rows_list.rows})
        # print(ret)
        self.write(json.dumps(ret))

    def post(self):
        """添加"""
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}
        caption = self.get_argument('caption', None)
        province_nid = self.get_argument('province_id', None)
        if not caption or not province_nid:
            ret['message'] = '输入不能为空'
        else:
            response = region_service.create_city(province_nid, caption)
            ret = response.__dict__
        self.write(json.dumps(ret))

    def put(self):
        """修改数据"""
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}
        nid = self.get_argument('nid', None)
        province_nid = self.get_argument('province_id', None)
        replace = self.get_argument('caption', None)
        if not nid or not province_nid or not replace:
            ret['message'] = '选择错误'
        else:
            response = region_service.modify_city(nid, province_nid, replace)
            ret = response.__dict__
        self.write(json.dumps(ret))

    def delete(self):
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}
        nid = self.get_argument('nid', None)
        if not nid:
            ret['message'] = '请选择要删除的市'
        else:
            response = region_service.delete_city(nid)
            ret = response.__dict__
        self.write(json.dumps(ret))


class CountyManagerHandler(AdminRequestHandler):
    """docstring for CountyManagerHandler"""

    def get(self):
        self.render('Region/CountyManager.html')


class CountyHandler(AdminRequestHandler):
    """docstring for CountyHandler"""

    def get(self):
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}
        if self.get_argument('type', None) == 'city':
            city_nid = self.get_argument('city_id', None)
            if not city_nid:
                ret['message'] = '请指定市ID'
            else:
                rows_list = region_service.get_county_by_city(city_nid)
                ret = rows_list.__dict__
        else:
            page = int(self.get_argument('page', 1))
            rows = int(self.get_argument('rows', 10))
            start = (page - 1) * rows

            rows_list = region_service.get_county_by_page(start, rows)
            rows_count = region_service.get_county_count()
            ret['success'] = all([rows_list.success, rows_count.success])
            ret['message'] = rows_list.message + '  ' + rows_list.message
            ret.update({'total': rows_count.rows, 'rows': rows_list.rows})
        # print(ret)
        self.write(json.dumps(ret))

    def post(self):
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}
        caption = self.get_argument('caption', None)
        city_nid = self.get_argument('city_id', None)
        if not caption or not city_nid:
            ret['message'] = '县（区）不能为空'
        else:
            response = region_service.create_county(city_nid, caption)
            ret = response.__dict__
        self.write(json.dumps(ret))

    def put(self):
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}

        nid = self.get_argument('nid', None)
        replace = self.get_argument('caption', None)
        city_nid = self.get_argument('city_id', None)
        if not nid or not replace or not city_nid:
            ret['message'] = '选择错误'
        else:
            response = region_service.modify_county(nid, city_nid, replace)
            ret = response.__dict__
        self.write(json.dumps(ret))

    def delete(self):
        Mapper.register(ModelRegionService, RegionRepository())
        Mapper.register(RegionService, ModelRegionService())
        region_service = RegionService()

        ret = {'success': False, 'message': ""}

        nid = self.get_argument('nid', None)
        if not nid:
            ret['message'] = '请选择要删除的县（区）'
        else:
            response = region_service.delete_county(nid)
            ret = response.__dict__
        self.write(json.dumps(ret))
