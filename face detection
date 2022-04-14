import cv2 as cv

# vid = cv.VideoCapture(0)
# while True:
#     success, img = vid.read()
#     cv.imshow("video", img)
#     if cv.waitKey(1) == ord("q"):
#         break

faceCascade= cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv.imread("trio.jpg")
imgGray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces= faceCascade.detectMultiScale(imgGray, 1.3, 5)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)

cv.imshow("result",img)
cv.waitKey(0)
