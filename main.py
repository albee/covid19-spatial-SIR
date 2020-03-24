from Cluster import Cluster
import math

dt = 0.001 # days
sim_iters = int(math.floor(30/dt))

boston = Cluster(sim_iters, 10000, 1, 0)

for i in range(sim_iters):
	boston.increment_model(dt)
	print i

boston.plot_cluster()