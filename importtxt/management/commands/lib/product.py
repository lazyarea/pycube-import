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
                    columns += ','.join(row)+')VALUES'
                    #for i in row: values += "'%s',"
                    #values = values[0:-1] + ')'
                #print("values" % ','.join(row))
                c += 1

        print(columns)
        print(values)
