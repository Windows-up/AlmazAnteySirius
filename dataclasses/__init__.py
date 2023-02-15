from numpy import ndarray


class ImageOutPoints:
    def __init__(self, garage: list, places: list, parking: list):
        self.garage = garage
        self.places = places
        self.parking = parking

    def __repr__(self):
        return f"garage: {len(self.garage)} | " \
               f"places: {len(self.places)} | " \
               f"parking: {len(self.parking)} "


class Filter:
    def __init__(self, lower: ndarray, upper: ndarray):
        self.upper = upper
        self.lower = lower
