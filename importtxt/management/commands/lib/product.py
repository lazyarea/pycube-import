import csv
import os
from lib.utils import *

NUMROWS = 3

class product:
    def __init__(self):
        super().__init__()

    def load_csv(self,fp):
        # print(settings.BASE_DIR)
        conn = utils().get_conn()
        c=0;
        rows = []
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                if c == 0:
                    c +=1
                    continue
                rows.append(row)
                if (c % NUMROWS == 0):
                    self.register_product(conn,rows)
                    rows = []
                c += 1
        conn.close()

    def register_product(self,conn=[],rows=[]):
        sql = '''INSERT INTO dtb_product(
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
'''
        vals = '''("{0[0]}","{0[1]}","{0[2]}","{0[3]}","{0[4]}","{0[5]}","{0[6]}","{0[7]}","{0[8]}")'''
        v = []
        for row in rows:  v.append(vals.format(row))
        # print(sql + ','.join(v))
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql + ','.join(v))
            # conn.commit()
                pass
        finally:
            # conn.close()
            pass
