import json
import numpy as np
from sklearn import linear_model, svm
from sklearn.neural_network import MLPRegressor
import pandas as pd
import sys
from datetime import datetime
import math

input_file = 'clean_data/combined_inspection_data.json'

def main():
    #File now contains number of health inspection violations respective to each business 
    input_file = 'clean_data/grouped_louisville_inspections_yelp_violations.json'

    with open(input_file, 'r') as f:
      data = dict(json.load(f))

    businesses = []

    #add params mutates 'data'!!!
    addParams(data)

    for d in data.values():

      # Only include restaurants with at least 3 inspections
      if len(d['scores']) >= 3:
        #If a violation count exists for this business, set it. If not, its 0.
        violation_count=0
        if(d['violations']): 
            violation_count = [d['violations']] 
        else: 
            violation_count=0

        avg_score = sum([score[2] for score in d['scores']]) / len(d['scores'])
        #Latitude and Longitude values with the inspection violation count in one variable

        inputs = [d['lat'], d['long'],d['violations']]
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
    neural = MLPRegressor(hidden_layer_sizes=(100), solver="sgd", activation="logistic",batch_size=len(train_data)/100,learning_rate="invscaling",learning_rate_init=.05)

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
