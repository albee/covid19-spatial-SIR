# Uses Kermack-McKendrick model, with spatial spread component between discrete steps
import numpy as np

class Cluster(object):

	def __init__(self, population="0", recovered="0", susceptible="0", infected="0", lat="45", lon="37", density="0"):
		self.population = population

		self.recovered = recovered
		self.susceptible = susceptible
		self.infected = infected

		self.lat = lat
		self.lon = lon

		self.density = density

		self.history

	def plot_cluster():
		pass

	# Update the spread model internally
	def increment_model(dt):
		s = self.susceptible
		i = self.infected
		r = self.recovered
		# factors: density, "R0 goodness"

	def plot_city():

	def increment_external():
		# factors: random connectedness, proximity random connectedness