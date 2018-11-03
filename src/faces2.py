import numpy as np
import cv2
from cv2 import face
import pickle
import time

# set start and end capture times to 0
startCapTime = 0
endCapTime = 0

# set previous ID to a null value
prevID_ = -1

# boolean to use on while loop for student attendance
studentAttended = False

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')

# import pdb; pdb.set_trace()
# print(help(cv2.face))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizers/face-trainner.yml")

labels = {"person_name": 1}
with open("pickles/face-labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v: k for k, v in og_labels.items()}

cap = cv2.VideoCapture(0)

while (studentAttended == False):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        # print(x,y,w,h)
        roi_gray = gray[y:y + h, x:x + w]  # (ycord_start, ycord_end)
        roi_color = frame[y:y + h, x:x + w]

        # recognize? deep learned model predict keras tensorflow pytorch scikit learn
        id_, conf = recognizer.predict(roi_gray)
        if conf >= 4 and conf <= 85:
            if prevID_ != id_:
                # if previous ID is not the same as current ID
                # update startCapTime to ensure 5 seconds must be reached
                startCapTime = time.perf_counter()

                # print("prevID_: " + str(prevID_) + " id_: " + str(id_))
            elif endCapTime - startCapTime > 5:
                # if previous ID is the same as current ID and it has been for over 5 seconds
                # here we need to assign attended!!!

                studentAttended = True
                # print(labels[id_] + " is present.")
                # print("end - start > 5 : " + str(endCapTime - startCapTime))
                # REMOVE ONCE ASSIGNMENT HAS BEEN ADDED
                # pass

            # always update the endCapTime
            endCapTime = time.perf_counter()

            # print(5: #id_)
            # print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            prevID_ = id_
        else:
            # else no longer recognizing
            # reset previous ID to a null value
            prevID_ = -1
            # possibly remove this!!!

        img_item = "7.png"
        cv2.imwrite(img_item, roi_color)

        color = (255, 0, 0)  # BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    #     	subitems = smile_cascade.detectMultiScale(roi_gray)
    #     	for (ex,ey,ew,eh) in subitems:
    #     		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # Display the resulting frames
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# this is where we could add attendance to the student
# print student who is in attendance
print(labels[prevID_] + ", Attendance: " + str(studentAttended))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
