import numpy as np

from dataclasses import Filter, ImageOutPoints
from analytics.cv_processing import get_filtered_points

RED_FILTERS = [
    Filter(np.array([0, 100, 20]), np.array([10, 255, 255])),
    Filter(np.array([160, 100, 20]), np.array([179, 255, 255])),
]
BLUE_FILTERS = [Filter(np.array([111, 95, 104]), np.array([170, 255, 255]))]

GREEN_FILTERS = [Filter(np.array([43, 95, 104]), np.array([113, 255, 255]))]


def get_image_out_point(image_name: str) -> ImageOutPoints:
    garage = get_filtered_points(image_name, GREEN_FILTERS)
    parking = get_filtered_points(image_name, BLUE_FILTERS)
    places = get_filtered_points(image_name, RED_FILTERS)

    return ImageOutPoints(garage, places, parking)
