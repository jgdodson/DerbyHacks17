# -*- coding: utf-8 -*-
# @Author: Miclain Keffeler
# @Date:   2017-02-25 10:15:52
# @Last Modified by:   Miclain Keffeler
# @Last Modified time: 2017-02-25 15:03:34
import csv
import os
import sys

linecount=0
input_file = 'raw_data/Health_InspViolations.csv'
output_file = 'clean_data/Health_InspViolations.csv'

#Open the input and output files
with open(input_file, 'r') as csvfile:
  rdr = csv.reader(csvfile)
  with open(output_file,"w") as csvfile1:
      wtr = csv.writer(csvfile1)
      #Add the appropriate column headers to the file
      entry='inspection_id,weight,critical_yn'
      new_header = entry[0:32]
      wtr.writerow([new_header])

      for line in rdr:
       #If this is not the first line in the file
        if(linecount!=0):
          linecount=linecount+1
          #Strip the double quotes and output
          clean_line = [entry.strip('"') for entry in line]
          wtr.writerow(clean_line)
        for line in rdr:
          #Add inspection id, weight to new row
          new_row = line[1:2]+line[4:5]

          #If the critical y/n value is No, add a 0 to new_row and write it
          if(line[5:6]==['No']):
            liste=[]
            liste=[0]
            new_row = line[1:2]+line[4:5]+liste[0:1]
            wtr.writerow(new_row)
          #Else, add a 1 to new_row and write it 
          else:
            lister=[]
            lister=[1]
            new_row = line[1:2]+line[4:5]+lister[0:1]
            wtr.writerow(new_row)        	
     