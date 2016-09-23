from Model.Merchant import IMerchantRepository
from Repository.DbConnection import DbConnection

class MerchantRepository(IMerchantRepository):
    """docstring for MerchantRepository"""
    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_merchant_count(self):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                count(1) AS count
            FROM
                merchant
        """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def fetch_merchant_by_page(self, start, rows):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                nid,
                name,
                domain
            FROM
                merchant
            ORDER BY
                nid DESC
            LIMIT % s OFFSET % s
        """
        cursor.execute(sql, (rows, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result     

    def fetch_merchant_detail_by_nid(self, nid):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                merchant.nid AS nid,
                name,
                domain,
                business_phone,
                business_mobile,
                qq,
                backend_mobile,
                backend_phone,
                address,
                user_id,
                county_id,
                county.caption AS county_caption
            FROM
                merchant
            LEFT JOIN userinfo ON merchant.user_id = userinfo.nid
            LEFT JOIN county ON merchant.county_id = county.nid
            WHERE
                merchant.nid =% s
        """
        cursor.execute(sql, (nid,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result

    def add_merchant(self, **kwargs):
        cursor = self.db_conn.connect()
        sql = """
            INSERT INTO merchant (% s)
            VALUES
                (% s)
        """
        key_list, value_list = [], []
        for k, v in kwargs.items():
            key_list.append(k)
            value_list.append('%%(%s)s' % k)
        sql = sql % (','.join(key_list), ','.join(value_list))
        cursor.execute(sql, kwargs)
        self.db_conn.close()


    def update_merchant(self, nid, **kwargs):
        cursor = self.db_conn.connect()
        sql = """
            UPDATE merchant
            SET % s
            WHERE
                nid =% s
        """
        value_list = []
        for k, v in kwargs.items():
            value_list.append('%s=%%(%s)s' %(k, k))
        sql = sql % (','.join(value_list), nid)
        cursor.execute(sql, kwargs)
        self.db_conn.close()

    def detete_merchant(self, nid):
        cursor = self.db_conn.connect()
        sql = """
            DELETE
            FROM
                merchant
            WHERE
                nid =% s
        """
        db_result = cursor.execute(sql, (nid,))
        self.db_conn.close()

        