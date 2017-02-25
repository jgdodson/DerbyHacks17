import json
import numpy as np
from sklearn import linear_model, svm
from sklearn.neural_network import MLPRegressor
import pandas as pd
import sys
from datetime import datetime
import math

complaintFile = open("./Data/Citizen311Data_STD.csv")
lines = complaintFile.readlines()
complaintFile.close()

output = open("./Data/Citizen311Data_STD.csv", w+)
