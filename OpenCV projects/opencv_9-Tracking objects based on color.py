import cv2
import numpy as np

width = 640
height = 360
# 1920x1080
# 640x360
# 320x180
# 1280x720

hueL = 10
hueH = 20
satL = 10
satH = 250
valL = 10
valH = 250

def onTrack1(val) :
    global hueL
    hueL = val
    print('hue low',hueL)

def onTrack2(val) :
    global hueH
    hueH = val
    print('hue high',hueH)

def onTrack3(val) :
    global satL
    satL = val
    print('sat low',satL)

def onTrack4(val) :
    global satH
    satH = val
    print('sat high',satH)

def onTrack5(val) :
    global valL
    valL = val
    print('val low',valL)

def onTrack6(val) :
    global valH
    valH = val
    print('val high',valH)


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTracker')
cv2.moveWindow("myTracker", width, 0)

cv2.createTrackbar('Hue Low', 'myTracker', 10, 179, onTrack1)
cv2.createTrackbar('Hue High', 'myTracker', 10, 179, onTrack2)
cv2.createTrackbar('Sat Low', 'myTracker', 10, 255, onTrack3)
cv2.createTrackbar('Sat High', 'myTracker', 250, 255, onTrack4)
cv2.createTrackbar('Val Low', 'myTracker', 10, 255, onTrack5)
cv2.createTrackbar('Val haig', 'myTracker', 250, 255, onTrack6)

while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame,1)

    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueL,satL,valL])
    upperBound = np.array([hueH,satH,valH])
    myMask = cv2.inRange(frameHSV,lowerBound,upperBound) # If in range turn pixels White. Else turn black.
    myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    
    myObjectSmall = cv2.resize(myObject, (int(width/2), int(height/2)))
    myMaskSmall = cv2.resize(myMask,(int(width/2), int(height/2)))
    cv2.imshow('My Object', myObjectSmall)
    cv2.imshow('myMask', myMaskSmall)

    cv2.moveWindow('My Object', int(width/2), height)
    cv2.moveWindow('myMask', 0, height)

    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 