# -*- coding: utf-8 -*-
# @Author: Miclain Keffeler
# @Date:   2017-02-26 02:04:21
# @Last Modified by:   Miclain Keffeler
# @Last Modified time: 2017-02-26 02:35:44

#IMPORTANT: The File that was used as complaintfile could not be uploaded due to size constraints
#Please visit data.louisvilleky.gov and find the 311 Call Database csv file to use when updating
import json
import numpy as np
from sklearn import linear_model, svm
from sklearn.neural_network import MLPRegressor
import pandas as pd
import sys
from datetime import datetime
import math
import csv
import json
import numpy as np
from sklearn import linear_model, svm
from sklearn.neural_network import MLPRegressor
import pandas as pd
import sys
from datetime import datetime
import math


#Open Complaint File, set panda to read CSV of file
complaintFile = open('Data/Citizen311Data_STD.csv','r+')
tabulated311 = pd.read_csv(complaintFile)
complaintFile.close()
#Counters/Parameters
linecount = 0
#Number of months to look back on
monthsBack=12
#Open output file, and setup output writer
output = open('clean_data/Citizen311Data_2017_STD.csv','w+')
#Open the input and output files
wtr = csv.writer(output)
#Write the column headers respective to data pulled
wtr.writerow(["service_request_id","requested_datetime","description","Latitude","longitude"])
#For every row in the file
for i,srid in enumerate(tabulated311.service_request_id):
	#Used to show percentage completed when running/rerunning the script
	pct = float(i)/float(len(tabulated311.service_request_id))*100.0
	print pct
	#If the requested datetime fits the neccesary format
	if len(str(tabulated311.requested_datetime[i])) >= 17 and len(str(tabulated311.requested_datetime[i])) <= 23:
		#Then setup the dates
		today = datetime.now()
		prev = datetime.strptime(str(tabulated311.requested_datetime[i]), "%Y-%m-%d %H:%M:%S")
		#If the date of the 311 call falls within the set time period (MonthsBack=12) 
		if((today - prev).days < (30.48*monthsBack)):
			#Write it to output
			wtr.writerow([tabulated311.service_request_id[i],tabulated311.requested_datetime[i],tabulated311.description[i],tabulated311.Latitude[i],tabulated311.longitude[i]])
