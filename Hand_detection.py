import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
hand_cascade=cv2.CascadeClassifier('hand.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,image=cap.read()
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #faces=face_cascade.detectMultiScale(grey,1.2,5)
    #eyes=eye_cascade.detectMultiScale(grey,1.2,5)
    hands=hand_cascade.detectMultiScale(grey,1.1,5)

    for (X,Y,W,H) in hands:
        print(X,Y,W,H)
        cv2.rectangle(image, (X, Y), (X + W, Y + H), (0, 255, 0), 2)
        #cv2.rectangle(grey, (X, Y), (X + W, Y + H), (255, 0, 0), 2)
        #roi_grey = grey[Y:Y + H, X:X + W]
        roi_color = image[Y:Y + H, X:X + W]

    cv2.imshow("image",image)
    #cv2.imshow("grey",grey)
    k=cv2.waitKey(1)
    if k==32:
        break
cap.release()
cv2.destroyAllWindows()