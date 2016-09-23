from Repository.DbConnection import DbConnection
from Model.Product import IProductRepository


class ProductRepository(IProductRepository):
    """docstring for ProductRepository"""
    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_page_by_merchant_id(self, merchant_id, start, rows):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                nid,
                title,
                img,
                category_id
            FROM
                product
            WHERE
                merchant_id =% s
            ORDER BY
                nid DESC
            LIMIT % s OFFSET % s
        """
        cursor.execute(sql, (merchant_id, rows, start,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_count_by_merchant_id(self, merchant_id):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                count(1) AS count
            FROM
                product
            WHERE
                merchant_id =% s
        """
        cursor.execute(sql, (merchant_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']


    def exist_product_by_pid(self, product_id):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                count(1) AS count
            FROM
                product
            WHERE
                nid =% s
        """
        cursor.execute(sql, (product_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def fetch_product_by_pid(self, product_id):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                nid,
                title
            FROM
                product
            WHERE
                nid =% s
        """
        cursor.execute(sql, (product_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result

    def fetch_product_by_id(self, merchant_id, product_id):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                nid,
                title
            FROM
                product
            WHERE
                merchant_id =% s
            AND nid =% s
        """
        cursor.execute(sql, (merchant_id, product_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result

    def add_product(self, product_dict, detail_list, img_list):
        """
        创建商品
        :param product_dict: 商品字典 {'title': 'x'}
        :param detail_list: [{'key': xx, 'value': 'xxx'}]
        :param img_list: [{'src': 'fa'},{'src': 'fa'}]
        :return:
        """
        product_sql = """
            INSERT INTO product (% s)
            VALUES
                (% s)
        """
        p_k_list = []
        p_v_list = []
        for k in product_dict.keys():
            p_k_list.append(k)
            p_v_list.append('%%(%s)s' % k)
        product_sql = product_sql % (','.join(p_k_list), ','.join(p_v_list),)
        cursor = self.db_conn.connect()
        cursor.execute(product_sql, (product_dict,))
        product_id = cursor.lastrowid()

        if detail_list:
            d = map(lambda x: x.update(product_id=product_id), detail_list)
            list(d)
            detail_sql = """
                INSERT INTO product_detail (% s)
                VALUES
                    (% s)
            """
            d_k_list = []
            d_v_list = []
            for k in detail_list[0].keys():
                d_k_list.append(k)
                d_v_list.append('%%(%s)s' % k)
            detail_sql = detail_sql % (','.join(d_k_list), ','.join(d_v_list),)
            cursor.executemany(detail_sql, (detail_list,))

            if img_list:
                i = map(lambda x: x.update(product_id=product_id), img_list)
                list(i)
                img_sql = """
                    INSERT INTO product_img (% s)
                    VALUES
                        (% s)
                """
                i_k_list = []
                i_v_list = []
                for k in img_list[0].keys():
                    i_k_list.append(k)
                    i_v_list.append('%%(%s)s' % k)
                img_sql = img_sql % (','.join(i_k_list), ','.join(i_v_list),)
                cursor.executemany(img_sql, (img_list,))
            self.db_conn.close()

    def fetch_price_by_product_id(self,merchant_id, product_id):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                price.nid AS nid,
                standard,
                price,
                selling_price,
                product_id
            FROM
                price
            LEFT JOIN product ON price.product_id = product.nid
            WHERE
                product.merchant_id =% s
            AND product_id =% s
            ORDER BY
                nid DESC
        """
        cursor.execute(sql, (merchant_id, product_id,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def add_price(self, price_dict):

        price_sql = """
            INSERT INTO price (% s)
            VALUES
                (% s)
        """
        p_k_list = []
        p_v_list = []
        for k in price_dict.keys():
            p_k_list.append(k)
            p_v_list.append('%%(%s)s' % k)
        price_sql = price_sql % (','.join(p_k_list), ','.join(p_v_list), )

        cursor = self.db_conn.connect()
        cursor.execute(price_sql, price_dict)
        self.db_conn.close()

    def update_price(self, nid, price_dict):

        sql = """
            UPDATE price
            SET % s
            WHERE
                nid =% s
        """
        value_list = []
        for k, v in price_dict.items():
            value_list.append('%s=%%(%s)s' % (k, k))
        sql = sql % (','.join(value_list), nid )

        cursor = self.db_conn.connect()
        cursor.execute(sql, price_dict)
        self.db_conn.close()

    def fetch_product_pv(self, product_id):

        sql = """
            SELECT
                timespan,
                count(nid) AS pv
            FROM
                product_view
            WHERE
                product_id =% s
            GROUP BY
                timespan
        """
        cursor = self.db_conn.connect(cursor=None)
        cursor.execute(sql, product_id)
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_product_uv(self, product_id):

        sql = """
            SELECT
                timespan,
                count(1) AS uv
            FROM
                (
                    SELECT
                        ip,
                        timespan,
                        count(1)
                    FROM
                        product_view
                    WHERE
                        product_id =% s
                    GROUP BY
                        timespan,
                        ip
                ) AS B
            GROUP BY
                timespan
        """
        cursor = self.db_conn.connect(cursor=None)
        cursor.execute(sql, product_id)
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def add_product_puv(self, product_id, ip, current_date, current_timestamp):
        sql = """
            INSERT INTO product_view (
                product_id,
                ip,
                ctime,
                timespan
            )
            VALUES
                (% s ,% s ,% s ,% s)
        """
        cursor = self.db_conn.connect(cursor=None)
        cursor.execute(sql, (product_id, ip, current_date, current_timestamp,))
        self.db_conn.close()


    def fetch_super_new_product(self):
        """
        获取首页新品上市的数据
        :return:
        """
        cursor = self.db_conn.connect()
        sql = """
        SELECT
            price.nid as nid,
            product.title as title,
            product.img as img,
            price.selling_price as selling_price,
            product.nid as product_id

        FROM
            super_product
        LEFT JOIN price ON super_product.price_id = price.nid
        LEFT JOIN product ON product.nid = price.product_id

        where super_product.super_type =1
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def fetch_super_excellent_product(self):
        """
        获取首页精品推荐数据
        :return:
        """
        cursor = self.db_conn.connect()
        sql = """
        SELECT
            price.nid as nid,
            product.title as title,
            product.img as img,
            price.selling_price as selling_price,
            product.nid as product_id

        FROM
            super_product
        LEFT JOIN price ON super_product.price_id = price.nid
        LEFT JOIN product ON product.nid = price.product_id

        where super_product.super_type =2
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_limit_price_and_product(self, subsite_caption):
        cursor = self.db_conn.connect()
        sql = """
            SELECT
                price.nid AS nid,
                product.title AS title,
                product.img AS img,
                price.selling_price AS selling_price,
                product.nid AS product_id
            FROM
                price
            LEFT JOIN product ON product.nid = price.product_id
            LEFT JOIN category ON product.category_id = category.nid
            LEFT JOIN upper_category ON category.favor_id = upper_category.nid
            LEFT JOIN subsite ON upper_category.favor_id = subsite.nid
            WHERE
                subsite.caption = % s
            ORDER BY
                price.nid DESC
            LIMIT 6 OFFSET 0
        """
        cursor.execute(sql, (subsite_caption,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def fetch_product_and_merchant(self, product_id):
        sql = """
            SELECT
                product.nid,
                product.title,
                product.img,
                merchant.name,
                merchant.business_phone,
                merchant.business_mobile,
                merchant.qq
            FROM
                product
            LEFT JOIN merchant ON product.merchant_id = merchant.nid
            WHERE
                product.nid = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchone()
        self.db_conn.close()
        return result

    def fetch_price_list(self, product_id):

        sql = """
            SELECT
                price.nid AS price_id,
                product.nid AS product_id,
                price.standard,
                price.price,
                price.selling_price
            FROM
                price
            LEFT JOIN product ON product.nid = price.product_id
            WHERE
                product.nid = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_price_detail(self, price_id):
        sql = """
            SELECT
                price.nid,
                price.standard,
                price.price,
                price.selling_price
            FROM
                price
            WHERE
                price.nid = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (price_id,))
        result = cursor.fetchone()
        self.db_conn.close()
        return result

    def fetch_image_list(self, product_id):
        sql = """
            SELECT
                src AS img
            FROM
                product_img
            WHERE
                product_img.product_id = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result


    def fetch_detail_list(self, product_id):
        sql = """
            SELECT
                name,
                value
            FROM
                product_detail
            WHERE
                product_detail.product_id = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_comment_list(self, product_id):
        sql = """
            SELECT
                content,
                username,
                comment.ctime
            FROM
                comment
            LEFT JOIN userinfo ON comment.user_id = userinfo.nid
            WHERE
                product_id = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id,))
        result = cursor.fetchall()
        self.db_conn.close()
        return result

    def fetch_comment_count(self, product_id, fine):
        """

        :param product_id: 商品ID
        :param fine: 1表示满意，2表示不满意
        :return:
        """
        sql = """
            SELECT
                count(1) AS count
            FROM
                comment
            WHERE
                product_id = % s
            AND fine = % s
        """
        cursor = self.db_conn.connect()
        cursor.execute(sql, (product_id, fine))
        result = cursor.fetchone()
        self.db_conn.close()
        return result['count']