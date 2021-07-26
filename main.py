import cv2

face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # the model I'm using
cap = cv2.VideoCapture(0) # by default your webc camera is = 0, however yours might be diff


while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # changing to gray
    face = face_casecade.detectMultiScale(gray, 1.5, 4)

    for (x, y, w, h) in face:
         cv2.rectangle(img, (x,y), (x+y , y+h), (0,255,0),2)

    cv2.imshow('img',img)
    key = cv2.waitKey(30) &0xff # to get out of the camera
    if key ==27:
        break
cap.release()