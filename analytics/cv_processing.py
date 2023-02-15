from typing import List

import cv2
import numpy as np

from dataclasses import Filter


def get_filtered_points(image_name: str, filters: List[Filter]):
    points = []

    image = cv2.imread(image_name)
    # cv2.imshow("Original", image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    full_mask = cv2.inRange(image, filters[0].lower, filters[0].upper)
    if len(filters) > 1:
        for i in range(1, len(filters)):
            filter = filters[i]
            full_mask += cv2.inRange(image, filter.lower, filter.upper)

    result = full_mask.copy()
    contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    colored_result = cv2.bitwise_and(image, image, mask=full_mask)

    for cont in contours:
        sm = cv2.arcLength(cont, True)
        apd = cv2.approxPolyDP(cont, 0.02 * sm, True)
        perimeter = cv2.arcLength(cont, True)
        # print(cv2.boxPoints(cv2.minAreaRect(cont)))

        rect = cv2.minAreaRect(cont)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        M = cv2.moments(cont)
        try:

            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            points.append((cx, cy))
            cv2.circle(colored_result, (cx, cy), 1, (255, 0, 0), 2)
        except ZeroDivisionError:
            pass

        cv2.drawContours(colored_result, [box], 0, (0, 0, 255), 2)

    # cv2.imshow('mask', full_mask)
    # cv2.imshow('mask', result)
    # cv2.imshow('result', colored_result)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return points
