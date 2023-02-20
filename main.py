import itertools
import time
import cv2

from analytics import get_image_out_point
import math

FILE_NAME = "images/dolgo.jpg"


def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def get_variants(data):
    return list(itertools.permutations(data.places))


if __name__ == '__main__':
    print("Image processing started")
    data = get_image_out_point(FILE_NAME)
    print("Image processing complited")
    minElement = 9999999999
    minPath = 0
    prev_proc = 0
    all_variants_len = math.factorial(len(data.places))
    print("math processing started")
    start_time = time.time()

    for i, variant in enumerate(itertools.permutations(data.places)):
        variant = list(variant)
        variant.insert(0, data.garage[0])
        variant.append(data.parking[0])
        summ = 0

        procents = int(i / all_variants_len * 100)
        if procents != prev_proc:
            print(f"Executed: {procents}%")
            prev_proc = procents

        for j in range(len(variant) - 1):
            summ += dist(variant[j], variant[j + 1])
            if summ > minElement:
                break
        else:
            if summ < minElement:
                minPath = variant
                minElement = summ

    print(f"{(time.time() - start_time)} seconds ")

    img = cv2.imread(FILE_NAME)

    for i in range(len(minPath) - 1):
        cv2.line(img, minPath[i], minPath[i + 1], (235, 161, 52), 3)

    cv2.imshow("result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(minElement, minPath)
