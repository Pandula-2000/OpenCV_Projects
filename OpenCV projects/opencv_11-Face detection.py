
import cv2

width = 360
height = 180
# 1920x1080
# 640x360
# 320x180
# 1280x720

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade = cv2.CascadeClassifier("harr\haarcascade_frontalface_default.xml")   # Create an object

while True:
    ignore, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frameGray, 1.3, 5)   # find the faces and put their location in the variable, faces
    print(faces)
    for face in faces:
        #x, y, w, h = face
        x = face[0]
        y = face[1]
        w = face[2]
        h = face[3]
        cv2.rectangle(frame, (x, y),(x+w,y+h), (255,0,0), 2)
    frame = cv2.flip(frame,1)
    cv2.imshow('cam1',frame)

    #cv2.imshow('Grey',frameGray)
    cv2.moveWindow('cam1',0,0)

    #cv2.moveWindow('Grey',0,0)
    



    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 