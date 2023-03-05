import csv

class CsvFileRead:
    def csvReader(self):
        file = open('university.csv',mode = 'r')
        csvfile = csv.reader(file)
        for row in csvfile:
            print(row)

csvfileread=CsvFileRead()
csvfileread.csvReader()

