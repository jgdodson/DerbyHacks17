import numpy as np
import matplotlib.pyplot as plt
import json

data_file = 'clean_data/combined_inspection_data.json'

with open(data_file, 'r') as f:
  data = dict(json.load(f))

lats = []
longs = []
weights = []

# weight data points based on their score
for d in data.values():
  if len(d['scores']) >= 5:
    lats.append(d['lat'])
    longs.append(d['long'])
    w = (100 - np.mean([s[2] for s in d['scores']]))**2
    weights.append(w)

lat_res = 0.02
long_res = 0.02

lat_mean  = np.mean(lats)
long_mean = np.mean(longs)

lat_std = np.std(lats)
long_std = np.std(longs)

lat_limits = [lat_mean - 0.1*lat_std, lat_mean + 0.1*lat_std]
long_limits = [long_mean - 0.1*long_std, long_mean + 0.05*long_std]

H, x_edges, y_edges = np.histogram2d(x=lats, y=longs, bins=500, range=[lat_limits, long_limits], normed=True, weights=weights)

X, Y = np.meshgrid(x_edges, y_edges)

fig = plt.figure()

ax = fig.add_subplot(111)

<<<<<<< HEAD
plt.pcolormesh(X, Y, H, vmin=0)
=======
plt.pcolormesh(X, Y, H)
>>>>>>> origin/Mkkeffeler1

plt.show()
