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
                    rows = []
                c += 1
                if ( c == FULLLINES & len(rows) > 0):
                    self.register_product(conn,rows)
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
                    r = cursor.execute(sql, (row))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])
        finally:
            # print('finally')
            pass

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
'''
