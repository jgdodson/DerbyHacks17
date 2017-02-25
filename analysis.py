import csv
import json

input_file = 'clean_data/clean_louisville_inspections_simple.csv'
output_file = 'clean_data/grouped_louisville_inspections.json'

def group_by_establishment(rows):
  groups = {}

  for row in rows:
    if row[0] in groups:
      groups[row[0]].append(row[1:])
    else:
      groups[row[0]] = [row[1:]]

  return groups

with open(input_file, 'r') as f:
  csv_reader = csv.reader(f)
  rows = [row for row in csv_reader]

groups = group_by_establishment(rows)

with open(output_file, 'w') as g:
  json.dump(groups, g)
