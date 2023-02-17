import itertools
from analytics import get_image_out_point, findDistance
import math




if __name__ == '__main__':
    data = get_image_out_point("images/test.jpg")
    minElement = 9999999999
    minPath = 0


    def dist(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

    all_variants = list(itertools.permutations(data.places))
    for i in range(len(all_variants)):
        variant = list(all_variants[i])
        variant.insert(0, data.garage)
        variant.append(data.parking)
        summ = 0
        for j in range(len(all_variants[i])):
            summ += dist(variant[j], variant[j+1])
            if summ < minElement:
                minPath = variant
                minElement = summ

    print(minElement, minPath)






