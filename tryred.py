import cv2
import numpy as np

points = []

image = cv2.imread('photo.jpg')
cv2.imshow("Original", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower boundary RED color range values; Hue (0 - 10)
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

# upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160, 100, 20])
upper2 = np.array([179, 255, 255])

lower_mask = cv2.inRange(image, lower1, upper1)
upper_mask = cv2.inRange(image, lower2, upper2)

full_mask = lower_mask + upper_mask

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

print(points)

# cv2.imshow('mask', full_mask)
cv2.imshow('mask', result)
cv2.imshow('result', colored_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
