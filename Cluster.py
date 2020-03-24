# Uses Kermack-McKendrick model, with spatial spread component between discrete steps
import numpy as np
from matplotlib import pyplot as plt 

class Cluster(object):

	def __init__(self, sim_iters=0, susceptible="0", infected="0", recovered="0", lat="45", lon="37", density="0"):
		self.population = recovered + susceptible + infected

		self.recovered = recovered
		self.susceptible = susceptible
		self.infected = infected
		self.time = 0

		self.lat = lat
		self.lon = lon

		self.density = density

		self.history = np.zeros((sim_iters+1, 4))
		self.history[0,:] = [self.time, susceptible, infected, recovered]  # [time, s, i, r]

		self.beta = 2.5/14/1000  # infection rate (per day)
		self.gamma = 1.0/14 # recovery rate (per day)

		self.sim_iters = sim_iters
		self.iter = 0

	def plot_cluster():
		pass

	# Update the spread model internally.
	# iter - iteration
	# dt - timestep in days
	def increment_model(self, dt):  
		s = self.susceptible
		i = self.infected
		r = self.recovered
		beta = self.beta
		gamma = self.gamma

		# factors to add: density, "R0 goodness"

		ds = -beta*s*i
		di = beta*s*i - gamma*i
		dr = gamma*i

		s += ds*dt
		i += di*dt
		r += dr*dt

		self.time += dt
		self.susceptible = s
		self.infected = i
		self.recovered = r
		print dr

		self.iter += 1
		self.history[self.iter,:] = [self.time, s, i, r]


	def plot_cluster(self):
		fig = plt.figure()
		plt.plot(self.history[:,0], self.history[:,1])  # s
		plt.plot(self.history[:,0], self.history[:,2])  # i
		plt.plot(self.history[:,0], self.history[:,3])  # r
		plt.legend(('susceptible', 'infected', 'recovered'))
		plt.show()

	def increment_external():
		# factors: random connectedness, proximity random connectedness
		pass