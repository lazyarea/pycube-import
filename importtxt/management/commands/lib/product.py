import csv

class product:
    def __init__(self):
        super().__init__()

    def load_csv(self,fp):
        c=0;
        columns = 'INSERT INTO ('
        values  = '('
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                if c == 0:
                    #columns += ','.join(row)+')VALUES'
                    #for i in row: values += "'%s',"
                    #values = values[0:-1] + ')'
                    c +=1
                    continue

                self.register_product([],row)
                c += 1


    def register_product(self,conn=[],data=[]):
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
({0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]},{0[8]})
'''
        print(sql.format(data))
