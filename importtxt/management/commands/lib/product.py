import csv
import os
from lib.utils import *

NUMROWS = 1

class product:
    def __init__(self):
        super().__init__()

    def load_csv(self,fp):
        # print(settings.BASE_DIR)
        conn = utils().get_conn()
        c=0;
        rows = []
        FULLLINES = len(open(fp).readlines()) # 行数取得
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)
            for row in csvreader:
                if c == 0 or row == []:
                    c +=1
                    continue
                rows.append(row)
                if (c % NUMROWS == 0):
                    self.register_product(conn,rows)
                    self.register_product_class(conn,rows)
                    self.register_product_image(conn,rows)
                    self.register_product_stock(conn,rows)
                    rows = []
                c += 1
                if ( c == FULLLINES & len(rows) > 0):
                    self.register_product(conn,rows)
                    self.register_product_class(conn,rows)
                    self.register_product_image(conn,rows)
                    self.register_product_stock(conn,rows)

        conn.close()

    def register_product(self,conn=[],rows=[]):
        if( len(rows) == 0): return
        sql = '''INSERT INTO dtb_product(
creator_id,
status,
name,
note,
description_list,
description_detail,
search_word,
free_area,
del_flg,
create_date,
update_date
)VALUES
(1, 1, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
#         vals = '''(%s, %s, %s, %s, %s, %s, %d, %s, %s)'''
        try:
            with conn.cursor() as cursor:
                # cursor.execute('select * from dtb_product;')
                # ret = cursor.fetchall()
                # print(ret)
                for row in rows:
                    r = cursor.execute(sql, (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])
            print('Got error')
        # finally:
        #     print('finally')
            # pass
        # print(sql)

    def register_product_class(self,conn=[],rows=[]):
        sql = '''
INSERT INTO dtb_product_class(
product_id,
product_type_id,
creator_id,
product_code,
stock,
stock_unlimited,
sale_limit,
price01,
price02,
delivery_fee,
create_date,
update_date,
del_flg
)
VALUES
((SELECT product_id FROM dtb_product WHERE name = %s LIMIT 1), (SELECT id FROM mtb_product_type WHERE name = %s), 1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
        try:
            with conn.cursor() as cursor:
                for row in rows:
                    r = cursor.execute(sql, (row[0],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[7],row[8],row[6]))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])
        except:
            print("Unexpected error:", sys.exc_info()[0])
        # finally:
        #     print('finally')
        #     pass

    def register_product_image(self,conn=[],rows=[]):
        sql = '''
INSERT INTO dtb_product_image(
product_id,
creator_id,
file_name,
rank,
create_date
)
VALUES
((SELECT product_id FROM dtb_product WHERE name = %s LIMIT 1), 1, %s, 0, %s)
'''
        try:
            with conn.cursor() as cursor:
                for row in rows:
                    r = cursor.execute(sql, (row[0],row[17],row[7]))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])
        #     print('Got error')

    def register_product_stock(self,conn=[],rows=[]):
        sql = '''
INSERT INTO dtb_product_stock(
product_class_id,
creator_id,
stock,
create_date,
update_date
)
VALUES
((SELECT product_class_id FROM dtb_product_class WHERE product_code = %s LIMIT 1), 1, %s, %s, %s)
'''
        try:
            with conn.cursor() as cursor:
                for row in rows:
                    r = cursor.execute(sql, (row[10],row[18],row[7],row[8]))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])
        #     print('Got error')
