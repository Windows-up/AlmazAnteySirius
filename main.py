import itertools
from analytics import get_image_out_point

if __name__ == '__main__':
    data = get_image_out_point("images/test.jpg")

    all_variants = list(itertools.permutations(data.places))
    print()
