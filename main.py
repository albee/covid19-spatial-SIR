# Keenan Albee and Antonio Teran

from Cluster import Cluster
import math
import numpy as np
import pandas as pd
from cities import City, get_cities_table, parse_cities


# Get the full city information as a table.
# data = get_cities_table("1000-largest-us-cities.csv")
# cities = parse_cities("1000-largest-us-cities.csv") # get an array with city objects.

# for c in cities:
#     print(c)

# Run a single city simulation
dt = 0.1 # days
sim_iters = int(math.floor(180/dt))

# boston = Cluster(sim_iters, 10000, 1, 0)
boston = Cluster(sim_iters, 4500000, 10000, 0)

for i in range(sim_iters):
	boston.increment_model(dt)

boston.plot_cluster()