import cv2 as cv
import numpy as np


def empty(a):
    pass


img = cv.imread("face.jpg")
# trackbars
cv.namedWindow("trackbars")
cv.resizeWindow("trackbars", 640, 240)
cv.createTrackbar("Hue min", "trackbars", 0, 179, empty)
cv.createTrackbar("Hue max", "trackbars", 179, 179, empty)
cv.createTrackbar("Sat min", "trackbars", 0, 255, empty)
cv.createTrackbar("Sat max", "trackbars", 255, 255, empty)
cv.createTrackbar("Val min", "trackbars", 0, 255, empty)
cv.createTrackbar("Val max", "trackbars", 255, 255, empty)

while True:
    size = cv.resize(img, (600, 400))
    imgHSV = cv.cvtColor(size, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue min", "trackbars")
    h_max = cv.getTrackbarPos("Hue max", "trackbars")
    s_min = cv.getTrackbarPos("Sat min", "trackbars")
    s_max = cv.getTrackbarPos("Sat max", "trackbars")
    v_min = cv.getTrackbarPos("Val min", "trackbars")
    v_max = cv.getTrackbarPos("Val max", "trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    higher = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, higher)  # defining lower and higher above
    # hor_img=np.hstack((size,size))

    result = cv.bitwise_and(size, size, mask=mask)
    cv.imshow("horizontal", imgHSV)
    cv.imshow("mask", mask)
    cv.imshow("color", result)
    # vertical = np.hstack((mask,mask))
    # cv.imshow("ver", vertical)

    if cv.waitKey(1) == ord('e'):
        break
