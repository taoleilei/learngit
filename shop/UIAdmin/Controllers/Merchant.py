from UIAdmin.Core.HttpRequest import AdminRequestHandler
from Service.Merchant.Service import MerchantService
from Model.Merchant import MerchantService as modelMerchantService
from Repository.MerchantRepository import MerchantRepository
from UIAdmin.Forms.Merchant import MerchantForm
from pymysql.err import IntegrityError
from Mapper import Mapper
import json


class MerchantManagerHandler(AdminRequestHandler):
    """docstring for MerchantManagerHandler"""

    def get(self):
        self.render('Merchant/MerchantManager.html')


class MerchantHandler(AdminRequestHandler):
    """docstring for MerchantHandler"""

    def get(self):
        # 依赖注入
        Mapper.register(modelMerchantService, MerchantRepository())
        Mapper.register(MerchantService, modelMerchantService())
        merchant_service = MerchantService()

        ret = {'success': False, 'message': ""}
        # MerchantManager.html发送过来的
        req_type = self.get_argument('type', None)
        if req_type == 'pagination':
            page = int(self.get_argument('page', 1))
            rows = int(self.get_argument('rows', 10))
            start = (page - 1) * rows
            rows_list = merchant_service.get_merchant_by_page(start, rows)
            rows_count = merchant_service.get_merchant_count()
            ret['success'] = all([rows_list.success, rows_count.success])
            ret['message'] = rows_list.message + rows_count.message
            ret.update({'total': rows_count.rows,
                        'rows': rows_list.rows})
            # print(ret)
            self.write(json.dumps(ret))
            return
        self.render('Merchant/MerchantManager.html')


class MerchantEditHandler(AdminRequestHandler):
    """docstring for MerchantEditHandler"""

    def get(self):
        form = MerchantForm()
        message = ''
        merchant_id = self.get_argument('nid', None)
        if not merchant_id:
            crumbs = '添加商户'
            method = 'POST'
            print(crumbs)
        else:
            crumbs = '编辑商户'
            # 依赖注入
            Mapper.register(modelMerchantService, MerchantRepository())
            Mapper.register(MerchantService, modelMerchantService())
            merchant_service = MerchantService()
            # 获取当前商户的详细信息
            detail = merchant_service.get_merchant_detail_by_nid(merchant_id)
            # print(detail.success)
            # print(detail.message)
            # print(detail.rows)
            # 获取错误信息，默认空字符串
            message = detail.message
            county_caption = detail.rows.pop('county_caption')
            county_id = detail.rows.get('county_id')
            form.county_id.widget.choices.append(
                {'value': county_id, 'text': county_caption})
            method = 'PUT'    # put方法用来做修改操作
            form.init_value(detail.rows)
        self.render('Merchant/MerchantEdit.html', form=form,
                    crumbs=crumbs, method=method, summary=message, nid=merchant_id)

    def post(self):
        """
        创建商户
        """
        method = self.get_argument('_method', None)

        if method == 'PUT':
            return self.put(self)

        message = ''
        form = MerchantForm()
        try:
            is_valid = form.valid(self)
            if is_valid:
                if form._value_dict['county_id'] == '0':
                    form._error_dict['county_id'] = '请选择县(区)ID'
                else:
                    del form._value_dict['nid']
                    del form._value_dict['city_id']
                    del form._value_dict['province_id']
                    print(form._value_dict)
                    # 依赖注入
                    Mapper.register(modelMerchantService, MerchantRepository())
                    Mapper.register(MerchantService, modelMerchantService())
                    merchant_service = MerchantService()

                    merchant_service.create_merchant(**form._value_dict)
                    self.redirect('/MerchantManager.html')
                    return
            else:
                form.init_value(form._value_dict)
        except IntegrityError as e:
            message = '商户名称或登陆用户必须唯一'
        except Exception as e:
            message = str(e)

        self.render('Merchant/MerchantEdit.html', form=form,
                    crumbs='添加商户', method='POST', summary=message, nid=None)

    def put(self):
        """
        修改
        """
        # 依赖注入
        Mapper.register(modelMerchantService, MerchantRepository())
        Mapper.register(MerchantService, modelMerchantService())
        merchant_service = MerchantService()

        message = ''
        form = MerchantForm()
        merchant_id = self.get_argument('nid', None)
        try:
            is_valid = form.valid(self)

            if is_valid:
                if form._value_dict['county_id'] == '0':
                    form._error_dict['county_id'] = '请选择县(区)ID'
                else:
                    nid = form._value_dict.pop('nid')
                    del form._value_dict['city_id']
                    del form._value_dict['province_id']

                    merchant_service.update_merchant(nid, **form._value_dict)
                    self.redirect('MerchantManager.html')
                    return
            else:
                form.init_value(form._value_dict)

        except Exception as e:
            message = str(e)

        detail = merchant_service.get_merchant_detail_by_nid(merchant_id)
        county_caption = detail.rows.pop('county_caption')
        county_id = detail.rows.get('county_id')
        form.county_id.widget.choices.append(
            {'value': county_id, 'text': county_caption})

        self.render('Merchant/MerchantEdit.html', form=form,
                    crumbs='编辑商户', method='PUT', summary=message, nid=merchant_id)

    def delete(self):
        """
        删除
        """
        # 依赖注入
        Mapper.register(modelMerchantService, MerchantRepository())
        Mapper.register(MerchantService, modelMerchantService())
        merchant_service = MerchantService()

        ret = {'success': False, 'message': ''}
        merchant_id = self.get_argument('nid', None)
        # print(merchant_id)
        if not merchant_id:
            ret['message'] = '请选着要删除的行'
        else:
            rows = merchant_service.delete_merchant(int(merchant_id))
            ret = rows.__dict__
        print(ret)
        self.write(json.dumps(ret))




