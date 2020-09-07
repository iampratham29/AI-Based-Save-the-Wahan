import cv2
import numpy as np

hand_cascade=cv2.CascadeClassifier('hand.xml')
cap=cv2.VideoCapture(0)

while True:
    stroke=0
    ret,image=cap.read()
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    grey1 = grey[:, :320]
    grey2 = grey[:, 320:]

    handr = hand_cascade.detectMultiScale(grey1, 1.1, 5)
    handl = hand_cascade.detectMultiScale(grey2, 1.1, 5)

    for (X,Y,W,H) in handl:
        stroke=1
        hand=1
        print("l")
    for (X,Y,W,H) in handr:
        stroke = 1
        hand = 2
        print("r")
    tmp=np.zeros((480,640))
    tmp1=image[:,320:]
    tmp2 = image[:, :320]
    cv2.imshow("image",image)

    k=cv2.waitKey(1)
    if k==32:
        break
cap.release()
cv2.destroyAllWindows()