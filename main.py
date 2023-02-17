import itertools

import cv2

from analytics import get_image_out_point
import math


def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def get_variants(data):
    return list(itertools.permutations(data.places))


if __name__ == '__main__':
    data = get_image_out_point("images/mine.jpg")
    minElement = 9999999999
    minPath = 0

    all_variants = get_variants(data)
    for i in range(len(all_variants)):
        variant = list(all_variants[i])
        variant.insert(0, data.garage[0])
        variant.append(data.parking[0])
        summ = 0
        for j in range(len(variant) - 1):
            summ += dist(variant[j], variant[j + 1])
        if summ < minElement:
            minPath = variant
            minElement = summ

    img = cv2.imread("images/mine.jpg")

    for i in range(len(minPath) - 1):
        cv2.line(img, minPath[i], minPath[i + 1], (235, 161, 52), 3)

    cv2.imshow("result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(minElement, minPath)
