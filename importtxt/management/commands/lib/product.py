import csv

class product:
    def __init__(self):
        super().__init__()

    def load_csv(self,fp):
        with open(fp, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                print(row)
