import csv

class ImportCSV:
    def __init__(self):
        self.csv = csv
    def import_csv(self):
        with open("newsacpractice/quickfix/quickfix.csv", mode="r") as f:
            reader = self.csv.reader(f)
            headers = next(reader)
            rows = list(reader)
            return headers, rows