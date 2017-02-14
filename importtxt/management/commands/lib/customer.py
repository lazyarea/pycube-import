import csv
import os
from lib.utils import *

NUMROWS = 1

class customer:
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
                    self.register_customer(conn,rows)
                    self.register_customer_address(conn,rows)
                    rows = []
                c += 1
                if ( c == FULLLINES & len(rows) > 0):
                    self.register_customer(conn,rows)
                    self.register_customer_address(conn,rows)

        conn.close()

    def register_customer(self,conn=[],rows=[]):
        if( len(rows) == 0): return
        sql = '''INSERT INTO dtb_customer(
status,
sex,
job,
country_id,
pref,
name01,
name02,
kana01,
kana02,
company_name,
zip01,
zip02,
zipcode,
addr01,
addr02,
email,
tel01,
tel02,
tel03,
fax01,
fax02,
fax03,
birth,
password,
salt,
secret_key,
first_buy_date,
last_buy_date,
buy_times,
buy_total,
note,
reset_key,
reset_expire,
create_date,
update_date,
del_flg
)VALUES
(1, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s)
'''
        try:
            with conn.cursor() as cursor:
                for row in rows:
                    for i in range(len(row)):
                        if (row[i] == 'NULL'): row[i] = None
                    # print(row)
                    r = cursor.execute(sql, (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9], \
                                        row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19], \
                                        row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28],row[29], \
                                        row[30],row[31],row[32],row[33],row[34]))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])

    def register_customer_address(self,conn=[],rows=[]):
        if( len(rows) == 0): return
        sql = '''INSERT INTO dtb_customer_address(
customer_id,
name01,
name02,
kana01,
kana02,
company_name,
zip01,
zip02,
zipcode,
addr01,
addr02,
tel01,
tel02,
tel03,
fax01,
fax02,
fax03,
create_date,
update_date,
del_flg
)VALUES
((SELECT customer_id FROM dtb_customer WHERE name01 = %s AND name02 = %s AND email = %s),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''
        try:
            with conn.cursor() as cursor:
                for row in rows:
                    for i in range(len(row)):
                        if (row[i] == 'NULL'): row[i] = None
                    r = cursor.execute(sql, (row[4],row[5],row[14],row[4],row[5],row[6],row[7],row[8],row[9],row[10], \
                                            row[11],row[12],row[13],row[15],row[16],row[17],row[18], \
                                            row[19],row[20],row[32],row[33],row[34]))
                conn.commit()
        except conn.InternalError as e:
            utils().log_info('Got error {!r}, errno is {}'.format(e, e.args[0]),[])
