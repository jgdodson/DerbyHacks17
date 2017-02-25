import json
import numpy as np
from sklearn import linear_model

input_file = 'clean_data/grouped_louisville_inspections.json'

with open(input_file, 'r') as f:
  data = dict(json.load(f))

pairs = []

for d in data.values():

  # Only include restaurants with at least 3 inspections
  if len(d['scores']) >= 3:
    avg_score = sum([score[2] for score in d['scores']]) / len(d['scores'])
    lat_long = [d['lat'], d['long']]
    pairs.append([lat_long, avg_score])

# Shuffle the data instances
np.random.shuffle(pairs)

# Split the data into train and test sets
train_data = pairs[:-200] 
test_data  = pairs[-200:]

# Split the train data into X and Y arrays
train_X = [d[0] for d in train_data]
train_Y = [d[1] for d in train_data]

# Split the test data into X and Y arrays
test_X = [d[0] for d in test_data] 
test_Y = [d[1] for d in test_data]

# Initialize the model
reg = linear_model.LinearRegression()

# Train the model
reg.fit(train_X, train_Y)

# Test the model
print(reg.score(test_X, test_Y))
