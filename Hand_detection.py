import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
hand_cascade=cv2.CascadeClassifier('hand.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    hands=hand_cascade.detectMultiScale(grey,1.1,5)

    for (X,Y,W,H) in hands:
        print(X,Y,W,H)
        cv2.rectangle(image, (X, Y), (X + W, Y + H), (0, 255, 0), 2)

        roi_color = image[Y:Y + H, X:X + W]
    tmp=np.zeros((480,640))
    tmp1=image[:,320:]
    tmp2 = image[:, :320]
    #cv2.imshow("image",image)

    cv2.imshow("sample", tmp1)
    cv2.imshow("sample2", tmp2)

    print(image.shape)
    k=cv2.waitKey(1)
    if k==32:
        break
cap.release()
cv2.destroyAllWindows()