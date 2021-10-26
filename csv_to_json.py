# Variable "the_file" has to be replaced with the name of the csv file to convert

import json
import csv
#import itertools

data = {}
the_file = "upwork target sample - collection.csv"
with open(the_file, "r") as to_convert:
    reader = csv.reader(to_convert)
    for each_row in reader:
        headers = [each_row[head] for head in range(len(each_row))]
        break
    del reader

    cvsReader = csv.DictReader(to_convert, fieldnames=headers)
    for row in cvsReader:
        cell_o = row[headers[0]]
        data[cell_o] = row

with open("CSV to JSON.json", "w") as to_json:
    to_json.write(json.dumps(data, indent=4))
