from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

#To check if your function works,
# a good practice is to add if __name__ == "__main__" at the end of distance.py and to compute a distance by calling the function:

if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 52.5200, 13.4050 # Berlin
    lat2, long2 = 51.0504, 13.7373 # Dresden
    #lat2, lon2 = x, y
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)
