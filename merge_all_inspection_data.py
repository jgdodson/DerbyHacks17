import csv
import json

pre_2017_data = 'raw_data/pre-2017-inspections.csv'
grouped_2017_data = 'clean_data/grouped_louisville_inspections.json'
output_file = 'clean_data/combined_inspection_data.json'

with open(grouped_2017_data, 'r') as f:
  data = dict(json.load(f))

with open(pre_2017_data, 'r') as f:
  csv_reader = csv.reader(f)

  for row in csv_reader:
    if row[0] in data and len(row[1]) > 0 and row[4] == 'REGULAR':
      old_date = str(row[2])
      mm, dd, yy = old_date[4:6], old_date[6:8], old_date[:4]
      new_date = '/'.join([mm,dd,yy])
      data[row[0]]['scores'].append(['',new_date,int(row[1])])

with open(output_file, 'w') as f:
  json.dump(data, f)

