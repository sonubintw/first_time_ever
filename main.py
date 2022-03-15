import cv2 as cv

cap=cv.VideoCapture(0)
cap.set(0,640)#height
cap.set(0,480)#width



while True:

    rand,vid = cap.read()

    cv.imshow("trial",vid)
    print(vid)

    if cv.waitKey(1) == ord('q'):
        break



