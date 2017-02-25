import csv

out = 'clean_data/clean_louisville_inspections.csv'

with open('raw_data/raw_louisville_inspections.csv', 'r') as f:
  r = csv.reader(f)
  with open(out, 'w') as g:
    w = csv.writer(g)
    for line in r:
      clean_line = [entry.strip('"') for entry in line]
      w.writerow(clean_line)


