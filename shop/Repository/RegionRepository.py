#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 4、实现业务接口
# 具体SQL语句，pymysql
from Model.Region import IRegionRepository
from Repository.DbConnection import DbConnection


class RegionRepository(IRegionRepository):
    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_province(self):
        cursor = self.db_conn.connect()
        sql = """select nid,caption from province order by nid desc"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_province_by_page(self, start, offset):
        cursor = self.db_conn.connect()
        sql = """select nid,caption from province order by nid desc limit %s offset %s"""
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def exist_province(self, caption):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from province where caption=%s"""
        cursor.execute(sql, (caption,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def add_province(self, caption):
        cursor = self.db_conn.connect()
        sql = """insert into province (caption) values (%s)"""
        cursor.execute(sql, (caption,))
        self.db_conn.close()

    def delete_province(self, province_nid):
        cursor = self.db_conn.connect()
        sql = """delete from province where nid = %s"""
        effect_rows = cursor.execute(sql, (province_nid,))
        self.db_conn.close()
        return effect_rows

    def update_province(self, province_nid, replace):
        cursor = self.db_conn.connect()
        sql = """update province set caption=%s where nid = %s"""
        effect_rows = cursor.execute(sql, (replace, province_nid,))
        self.db_conn.close()
        return effect_rows

    def fetch_province_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from province"""
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def fetch_city_by_province(self, province_nid):
        cursor = self.db_conn.connect()
        sql = """select nid, caption from city where province_id = %s order by city.nid desc"""
        cursor.execute(sql, (province_nid,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_city_by_page(self, start, offset):
        cursor = self.db_conn.connect()
        sql = """select city.nid as nid, city.caption as caption, province.caption as province, city.province_id as province_id from city left join province on city.province_id=province.nid order by city.nid desc limit %s offset %s"""
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_city_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from city"""
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def exist_city(self, province_nid, caption):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from city where caption=%s and province_id=%s"""
        cursor.execute(sql, (caption, province_nid))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def add_city(self, province_nid, caption):
        cursor = self.db_conn.connect()
        sql = """insert into city (caption,province_id) values (%s,%s)"""
        effect_rows = cursor.execute(sql, (caption, province_nid))
        self.db_conn.close()
        return effect_rows

    def delete_city(self, city_nid):
        cursor = self.db_conn.connect()
        sql = """delete from city where nid = %s"""
        effect_rows = cursor.execute(sql, (city_nid,))
        self.db_conn.close()
        return effect_rows

    def update_city(self, nid, province_nid, replace):
        cursor = self.db_conn.connect()
        sql = """update city set caption=%s, province_id=%s where nid = %s"""
        effect_rows = cursor.execute(sql, (replace, province_nid, nid))
        self.db_conn.close()
        return effect_rows

    def fetch_county_by_page(self, start, offset):
        cursor = self.db_conn.connect()
        sql = """select county.nid as nid, county.caption as caption, city.caption as city, county.city_id as city_id, province.caption as province, city.province_id as province_id from county left join city on county.city_id=city.nid left join province on city.province_id=province.nid order by county.nid desc limit %s offset %s"""
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_county_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from county """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def exist_county(self, city_id, caption):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from county where caption=%s and city_id=%s"""
        cursor.execute(sql, (caption, city_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def add_county(self, city_nid, caption):
        cursor = self.db_conn.connect()
        sql = """insert into county (caption,city_id) values (%s,%s)"""
        effect_rows = cursor.execute(sql, (caption, city_nid))
        self.db_conn.close()
        return effect_rows

    def delete_county(self, county_nid):
        cursor = self.db_conn.connect()
        sql = """delete from county where nid = %s"""
        effect_rows = cursor.execute(sql, (county_nid,))
        self.db_conn.close()
        return effect_rows

    def update_county(self, nid, city_nid, replace):
        cursor = self.db_conn.connect()
        sql = """update county set caption=%s, city_id=%s where nid = %s"""
        effect_rows = cursor.execute(sql, (replace, city_nid, nid))
        self.db_conn.close()
        return effect_rows

    def fetch_county_by_city(self, city_nid):
        cursor = self.db_conn.connect()
        sql = """select nid, caption from county where city_id=%s order by county.nid desc"""
        cursor.execute(sql, (city_nid,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result
