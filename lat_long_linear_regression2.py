import json
import numpy as np
from sklearn import linear_model, svm
from sklearn.neural_network import MLPRegressor
import pandas as pd
import sys
from datetime import datetime
import math

<<<<<<< HEAD
input_file = 'clean_data/combined_inspection_data.json'

# Load the dataset
with open(input_file, 'r') as f:
  data = dict(json.load(f))

# Pairs of inputs and targets for regression
pairs = []

for d in data.values():
  # Only include restaurants with at least 3 inspections
  if 10 <= len(d['scores']) <= 30:
    avg_score = np.mean([score[2] for score in d['scores']])
    lat_long = [d['lat'], d['long']]
    pairs.append([lat_long, avg_score])

def main():

    input_file = 'clean_data/grouped_louisville_inspections.json'

    with open(input_file, 'r') as f:
      data = dict(json.load(f))

    pairs = []

    #add params mutates 'data'!!!
    addParams(data)

    for d in data.values():

      # Only include restaurants with at least 3 inspections
      if len(d['scores']) >= 3:
        avg_score = sum([score[2] for score in d['scores']]) / len(d['scores'])
        lat_long = [d['lat'], d['long']]
        pairs.append([lat_long, avg_score])

    # Shuffle the data instances
    np.random.shuffle(pairs)

    # Split the data into train and test sets
    train_data = pairs[:-100]
    test_data  = pairs[-100:]

    # Split the train data into X and Y arrays
    train_X = [d[0] for d in train_data]
    train_Y = [d[1] for d in train_data]

    # Split the test data into X and Y arrays
    test_X = [d[0] for d in test_data]
    test_Y = [d[1] for d in test_data]

    # Initialize the model
    reg = linear_model.LinearRegression()
    svreg = svm.SVR()
    neural = MLPRegressor(hidden_layer_sizes=(100), solver="lbfgs", activation="logistic")

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
