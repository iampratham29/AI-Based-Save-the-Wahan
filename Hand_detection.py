import cv2
import numpy as np

hand_cascade=cv2.CascadeClassifier('hand.xml')
cap=cv2.VideoCapture(0)

while True:
    ret,image=cap.read()
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    grey1 = grey[:, :320]
    grey2 = grey[:, 320:]

    handl = hand_cascade.detectMultiScale(grey1, 1.1, 5)
    handr = hand_cascade.detectMultiScale(grey2, 1.1, 5)

    for (X,Y,W,H) in handl:
        # print(X,Y,W,H)
        cv2.rectangle(image, (X, Y), (X + W, Y + H), (0, 255, 0), 2)
        print(1)
        roi_color = image[Y:Y + H, X:X + W]
    for (X,Y,W,H) in handr:
        # print(X,Y,W,H)
        cv2.rectangle(image, (X, Y), (X + W, Y + H), (0, 255, 0), 2)
        print(2)
        roi_color = image[Y:Y + H, X:X + W]
    tmp=np.zeros((480,640))
    tmp1=image[:,320:]
    tmp2 = image[:, :320]
    #cv2.imshow("image",image)

    cv2.imshow("sample", tmp1)
    cv2.imshow("sample2", tmp2)

    # print(image.shape)
    k=cv2.waitKey(1)
    if k==32:
        break
cap.release()
cv2.destroyAllWindows()