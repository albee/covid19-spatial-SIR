# Keenan Albee and Antonio Teran
# Uses Kermack-McKendrick model, with spatial spread component between discrete steps
import numpy as np
from matplotlib import pyplot as plt 
import time

# LaTeX formatting
from matplotlib import rc
rc('font',**{'family':'DejaVu Sans','serif':['Computer Modern'], 'size': 18})
rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] # include a package

class Cluster(object):

	def __init__(self, sim_iters=0, susceptible="0", infected="0", recovered="0", lat="45", lon="37", density="0", name="empty"):
		self.N = recovered + susceptible + infected

		self.recovered = float(recovered)/self.N
		self.susceptible = float(susceptible)/self.N
		self.infected = float(infected)/self.N
		self.time = 0

		self.lat = lat
		self.lon = lon

		self.density = density

		self.history = np.zeros((sim_iters+1, 4))
		self.history[0,:] = [self.time, self.susceptible, self.infected, self.recovered]  # [time, s, i, r]

		self.R0 = 1.7#2.2  # R0 (approx)
		self.gamma = 1.0/12.0 # recovery rate (per day): inverse of infectious duration
		self.beta = self.R0*self.gamma # transmissibility x rate of contact (per day)

		self.sim_iters = sim_iters
		self.iter = 0

		self.name = name

	# Update the spread model internally.
	# iter - iteration
	# dt - timestep in days
	def increment_model(self, dt):  
		s = self.susceptible
		i = self.infected
		r = self.recovered
		gamma = self.gamma
		beta = self.beta

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
		print(s+i+r)
		# time.sleep(0.5)

		self.iter += 1
		self.history[self.iter,:] = [self.time, s, i, r]


	def plot_cluster(self):
		fig = plt.figure()
		plt.plot(self.history[:,0], self.N*self.history[:,1])  # s
		plt.plot(self.history[:,0], self.N*self.history[:,2])  # i
		plt.plot(self.history[:,0], self.N*self.history[:,3])  # r
		
		plt.legend(('susceptible', 'infected', 'recovered'))
		ax = plt.gca()
		ax.set_xlabel('Time since Mar-24 (days)')	
		ax.set_ylabel('Predicted number of people in category (people)')
		plt.title('Case Evolution, $R_0=1.7$')
		plt.show()

	def increment_external():
		# factors: random connectedness, proximity random connectedness
		pass