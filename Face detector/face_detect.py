import cv2 as cv

face_cascade = cv.CascadeClassifier('haar_face.xml')

vid = cv.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    # cv.imshow('Frame', frame)

    # convert video to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray', gray)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # print(faces)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)

    cv.imshow('FACE DETECTED', frame)
    if cv.waitKey(60) & 0xFF == ord('q'):
        break