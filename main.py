from Cluster import Cluster
import math

dt = 0.1 # days
sim_iters = int(math.floor(180/dt))

# boston = Cluster(sim_iters, 10000, 1, 0)
boston = Cluster(sim_iters, 4500000, 10000, 0)

for i in range(sim_iters):
	boston.increment_model(dt)

boston.plot_cluster()