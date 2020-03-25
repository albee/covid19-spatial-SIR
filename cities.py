# -*- coding: utf-8 -*-
"""Cities module"""

import csv
import pandas as pd


class City(object):
    """Bundle city properties in single object."""

    def __init__(self, name, rank, state, growth, population, latc, longc):
        """Create a city with all parameters.

        Args:
            name (string): name of the city.
            rank (int): do not know what this is.
            state (string): name of the state.
            growth (float): growth from 2000 to 2013.
            population (int): number of people.
            coords (tuple, float): latitude and longitude coordinates.
        """
        self.name = name
        self.rank = rank
        self.state = state
        self.growth = growth
        self.population = population
        self.latitude = latc
        self.longitude = longc
        self.coords = (latc, longc)

    def __repr__(self):
        return "{}, {}, population: {}".format(
            self.name, self.state, self.population)

    def set_name(self, name):
        self.name = name

    def set_rank(self, rank):
        self.rank = rank

    def set_state(self, state):
        self.state = state

    def set_growth(self, growth):
        self.growth = growth

    def set_population(self, population):
        self.population = population

    def set_coordinates(self, latc, longc):
        self.coords = (latc, longc)

    def get_name(self):
        return self.name

    def get_rank(self):
        return self.rank

    def get_state(self):
        return self.state

    def get_growth(self):
        return self.growth

    def get_population(self):
        return self.population

    def get_coordinates(self):
        return self.coords


def get_cities_table(csvf):
    """Parses city file and returns pandas dataframe.

    Args:
        csvf (string): path to csv file with city information.

    Returns:
        df (DataFrame): pandas dataframe with tabulated information.
    """
    return pd.read_csv(csvf, delimiter=';')


def parse_cities(csvf):
    """Parses a file with city information.

    Args:
        csvf (string): path to csv file with city information.

    Returns:
        cities (array, City): an array with City objects.

    """
    cities = []
    data = get_cities_table(csvf)
    # For each entry, create a city and append to array.
    for index, row in data.iterrows():
        coords = row['Coordinates'].split(',')
        city = City(row['City'], int(row['Rank']), row['State'], float(
            row['Growth From 2000 to 2013']), int(row['Population']),
            float(coords[0]), float(coords[1]))
        cities.append(city)
    return cities
