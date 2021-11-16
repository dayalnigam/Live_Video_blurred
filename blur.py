

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    status, photo = cap.read()
    model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    detect = model.detectMultiScale(photo)
    if len(detect)==0:
        print("no faces")
    else:
        for x,y,w,h in detect:
           a=cv2.rectangle(photo,(x,y),(x+w,y+h),[0,255,0],1)
           a[y:y+h,x:x+w] = cv2.medianBlur(a[y:y+h,x:x+w],35)

        cv2.imshow("Video ", photo)
        cv2.imshow("cropped",a[y:y+h,x:x+w])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


