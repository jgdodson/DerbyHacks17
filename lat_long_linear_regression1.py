import json
import numpy as np
from sklearn import linear_model, svm
from sklearn.neural_network import MLPRegressor
import pandas as pd
import sys
from datetime import datetime
import math

def addParams(dataDict):
    radius311 = .1
    maxMonthsBack = 12
    get311General(dataDict, radius311, maxMonthsBack)

#model attribute generators should only add new keys to dict
def get311General(dataDict, radius, monthsBack):
    #311cleanup.py is used to limit the number of 311 searchable calls down to a given time period (12 months as of now), speeding up run time considerably
    #If this time period is to be changed, please run 311cleanup with updated parameter and change the parameter here (maxMonthBack)
    complaintFile = open("clean_data/Citizen311Data_2017_STD.csv")
    tabulated311 = pd.read_csv(complaintFile)
    complaintFile.close()

    for entry in dataDict.values():
        entry["general311Incidents"] = 0

    for i,srid in enumerate(tabulated311.service_request_id):
        pct = float(i)/float(len(tabulated311.service_request_id))*100.0
        print pct
        if len(str(tabulated311.requested_datetime[i])) >= 17 and len(str(tabulated311.requested_datetime[i])) <= 23:
            today = datetime.now()
            prev = datetime.strptime(str(tabulated311.requested_datetime[i]), "%Y-%m-%d %H:%M:%S")
            if( (today - prev).days < 30.48*monthsBack):
                incidentLat = tabulated311.Latitude[i]
                incidentLong = tabulated311.longitude[i]
                for entry in dataDict.values():
                    if(math.hypot(incidentLat-entry["lat"], incidentLong - entry["long"]) < radius):
                        entry["general311Incidents"] += 1





def main():
    #File now contains number of health inspection violations respective to each business 

    input_file = 'clean_data/grouped_louisville_inspections_yelp_violations.json'

    with open(input_file, 'r') as f:
      data = dict(json.load(f))

    businesses = []
    ins = []
#Hard code the decimal values for total occurences of 1 inspection->12 inspections (at one business)
    ins.append(1018/4199)
    ins.append(2320/4199)
    ins.append(461/4199)
    ins.append(299/4199)
    ins.append(25/4199)
    ins.append(60/4199)
    ins.append(3/4199)
    ins.append(10/4199)
    #No businesses had 9 inspections
    ins.append(0)
    ins.append(2/4199)
    #No businesses had 11 inspections
    ins.append(0)
    ins.append(1/4199)

    #add params mutates 'data'!!!
    addParams(data)

    total_score = 0
    score_count = 0
    for d in data.values():
      
      inspection_count=0
      total_score=0

      # Only include restaurants with at least 3 inspections
      if len(d['scores']) >= 3:
        #If a violation count exists for this business, set it. If not, its 0.
        violation_count=0
        if(d['violations']): 
            violation_count = [d['violations']] 
        else: 
            violation_count=0
      #For every inspection that this business had
        for score in d['scores']:
            #Add 1 to inspection count
            inspection_count = inspection_count+1
            total_score += score[2]

        avg_score = total_score/inspection_count
        #Latitude and Longitude values with the inspection violation count in one variable

        inputs = [d['lat'], d['long'],d['violations'], ins[score_count-1]]
        businesses.append([inputs, avg_score])

    # Shuffle the data instances
    np.random.shuffle(businesses)

    # Use all the data except for the last 100 businesses as training, rest are testing
    train_data = businesses[:-100]
    test_data  = businesses[-100:]

    # Split the train data into X and Y and Z arrays
    train_X = [d[0] for d in train_data]
    train_Y = [d[1] for d in train_data]

    # Split the test data into X and Y arrays
    test_X = [d[0] for d in test_data]
    test_Y = [d[1] for d in test_data]


    # Initialize the model
    reg = linear_model.LinearRegression()
    svreg = svm.SVR()
    neural = MLPRegressor(hidden_layer_sizes=(100), solver="sgd", activation="logistic",learning_rate="invscaling",learning_rate_init=.05)

    # Train the model
    reg.fit(train_X, train_Y)
    svreg.fit(train_X, train_Y)
    neural.fit(train_X,train_Y)
   




    # Test the model
    print('Linear Reg: {}'.format(reg.score(test_X, test_Y)))
    print('SVG Reg: {}'.format(svreg.score(test_X, test_Y)))
    print('neural MLPRegressor: {}'.format(neural.score(test_X, test_Y)))

if __name__ == "__main__":
    main()


