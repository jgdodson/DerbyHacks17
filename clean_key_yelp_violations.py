# -*- coding: utf-8 -*-
# @Author: Miclain Keffeler
# @Date:   2017-02-25 13:27:49
# @Last Modified by:   Miclain Keffeler
# @Last Modified time: 2017-02-25 15:05:04
import csv
import os
import sys

linecount=0
counter=0
idlist = {}
prev_row = 0
liste=[]
#Open the original input file
input_file = 'raw_data/yelpdata/violations.csv'
output_file = 'clean_data/yelp_clean_violations.csv'
with open(input_file, 'r') as csvfile:
  rdr = csv.reader(csvfile)

  #Open the output file
  with open(output_file,"w") as csvfile1:
      wtr = csv.writer(csvfile1)

      for line in rdr:
#If this is not our first line
        if(linecount!=0):
          linecount=linecount+1
          #Strip the double quotes and write it
          clean_line = [entry.strip('"') for entry in line]
          wtr.writerow(clean_line)
        new_row = line[0:1]
#If the next line in the file is the same business
        if (str(new_row) == str(prev_row)):
          #Add 1 to violation count
          counter = counter+1
          liste=[counter]
          #Previous Row is Current Row
          prev_row = new_row
        #If there are no more appearances of this business ID
        else: 
#Put the count of violations next to its corresponding business_ID 
          new_row = line[0:1]+ liste[0:1]
          wtr.writerow(new_row)
          #Reset to continue
          prev_row=line[0:1]
          counter=0
          liste=[counter]        	
     