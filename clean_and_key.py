import csv
import os
import sys

linecount=0
with open('Data/Health_InspViolations.csv', 'r') as csvfile:
  rdr = csv.reader(csvfile)
  with open("CleanData/Health_InspViolations.csv","w") as csvfile1:
      wtr = csv.writer(csvfile1)
      entry='inspection_id,weight,critical_yn'
      new_header = entry[0:32]
      wtr.writerow([new_header])
      for line in rdr:
        if(linecount!=0):
          linecount=linecount+1
          clean_line = [entry.strip('"') for entry in line]
          wtr.writerow(clean_line)
        for line in rdr:
          new_row = line[1:2]+line[4:5]
          #wtr.writerow(new_row)
          if(line[5:6]==['No']):
            liste=[]
            liste=[0]
            new_row = line[1:2]+line[4:5]+liste[0:1]
            wtr.writerow(new_row)
          else:
            lister=[]
            lister=[1]
            new_row = line[1:2]+line[4:5]+lister[0:1]
            wtr.writerow(new_row)
         
        
          #new_row = line[0:1] + line[4:5] + line[5:6]
        	
     