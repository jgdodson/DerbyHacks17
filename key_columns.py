import csv

input_name = 'raw_data/raw_louisville_inspections.csv'
output_name = 'clean_data/clean_louisville_inspections_simple.csv'

with open(input_name, 'r') as f:
  csv_reader = csv.reader(f)
  with open(output_name, 'w') as g:
    csv_writer = csv.writer(g)
    for line in csv_reader:
      new_row = line[:2] + line[8:12] + [line[12][:10]] + [line[13]]
      csv_writer.writerow(new_row)
