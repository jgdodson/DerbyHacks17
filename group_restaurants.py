# -*- coding: utf-8 -*-
# @Author: Miclain Keffeler & Jordan Dodson (@PilgrimShadow)
# @Date:   2017-02-25 15:05:33
# @Last Modified by:   Miclain Keffeler
# @Last Modified time: 2017-02-25 15:08:57

import csv
import json

#Input and output file path delcarations
output_file = 'clean_data/grouped_louisville_inspections_yelp_violations.json'
input_file2 = 'clean_data/yelp_clean_violations.csv'

#Function used to combine 2 input files into one summary of characteristics for each unique business_id
def group_by_establishment(rows,rows1):
  groups = {}

  for row in rows:
    #If this business_id is already in the dictionary
    if row[0] in groups:
      groups[row[0]]['scores'].append([row[1], row[6], int(row[7])])
    else:
      #Otherwise, check inspection violations for a matching business_id
      for row1 in rows1:
        print row1[0],row[0]
        #If you found a match, print it to dictionary with the number of violations
        if row[0] == row1[0]:
         groups[row[0]] = {'violations': int(row1[1]), 'zip': int(row[2]), 'lat': float(row[4]), 'long': float(row[5]), 'type': row[3], 'scores': [[row[1], row[6], int(row[7])]]}

  return groups

#Open 2 input files
with open(input_file, 'r') as f:
  with open(input_file2,'r') as g:
    csv_reader = csv.reader(f)
    csv_reader1 = csv.reader(g)
    #Setup the recursive call to said function
    rows = [row for row in csv_reader]
    rows1 = [row1 for row1 in csv_reader1]  
  groups = group_by_establishment(rows[1:],rows1[1:])

#Put data in json file
with open(output_file, 'w') as g:
  json.dump(groups, g)
