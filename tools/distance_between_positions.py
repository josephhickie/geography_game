import numpy as np

EARTH_MEAN_RADIUS = 6371

def distance_between_positions(latitude1, longitude1, latitude2, longitude2):

    phi1 = latitude1 * (np.pi / 180)
    phi2 = latitude2 * (np.pi / 180)
    lambda1 = longitude1 * (np.pi / 180)
    lambda2 = longitude2 * (np.pi / 180)

    a = np.sin((phi2 - phi1) / 2)**2 + (
            np.cos(phi1) * np.cos(phi2) * np.sin((lambda2 - lambda1) / 2)**2
    )

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    d = EARTH_MEAN_RADIUS * c

    return d


def distance_between_two_cities(city1, city2):

    return distance_between_positions(
        city1['CapitalLatitude'], city1['CapitalLongitude'], city2['CapitalLatitude'], city2['CapitalLongitude']
    )
