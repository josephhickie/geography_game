import numpy as np

from tools import read_csv


def get_two_random_cities(file='/Users/joseph/PycharmProjects/geography_game/data/concap.csv'):

    df = read_csv(file)

    max_integer = len(df) + 1

    city1 = df.iloc[np.random.randint(0, max_integer)]
    city2 = df.iloc[np.random.randint(0, max_integer)]

    while city1['CountryName'] == city2['CountryName']:
        city2 = df.iloc[np.randint(0, max_integer)]

    return city1, city2