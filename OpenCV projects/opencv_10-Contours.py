import cv2
from cv2 import RETR_EXTERNAL
import numpy as np

width = 640
height = 360
# 1920x1080
# 640x360
# 320x180
# 1280x720

hueL = 10
hueH = 20
hueL1 = 10
hueH1 = 20
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

def onTrack10(val) :
    global hueL1
    hueL1 = val
    print('hue low1',hueL1)

def onTrack20(val) :
    global hueH1
    hueH1 = val
    print('hue high1',hueH1)

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
cv2.resizeWindow("myTracker",400,400)

cv2.createTrackbar('Hue Low', 'myTracker', 10, 179, onTrack1)
cv2.createTrackbar('Hue High', 'myTracker', 10, 179, onTrack2)
cv2.createTrackbar('Hue1 Low', 'myTracker', 10, 179, onTrack10)
cv2.createTrackbar('Hue1 High', 'myTracker', 10, 179, onTrack20)
cv2.createTrackbar('Sat Low', 'myTracker', 10, 255, onTrack3)
cv2.createTrackbar('Sat High', 'myTracker', 250, 255, onTrack4)
cv2.createTrackbar('Val Low', 'myTracker', 10, 255, onTrack5)
cv2.createTrackbar('Val High', 'myTracker', 250, 255, onTrack6)

while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame,1)

    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueL,satL,valL])
    upperBound = np.array([hueH,satH,valH])

    lowerBound1 = np.array([hueL1,satL,valL])
    upperBound1 = np.array([hueH1,satH,valH])

    myMask = cv2.inRange(frameHSV,lowerBound,upperBound) # If in range turn pixels White. Else turn black.
    myMask1 = cv2.inRange(frameHSV,lowerBound1,upperBound1)
    compositeMask = myMask | myMask1    # Combine 2 masks...( compositeMask = cv2.Add(mask1,mask2) will work too. ) 

    contours, junk = cv2.findContours(compositeMask, RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours :
        area = cv2.contourArea(contour)
        if area>=50 :
            #cv2.drawContours(frame,[contour], 0, (255,0,0), 3)  # Pass all the contours to this
            x, y, w, h, = cv2.boundingRect(contour)   # Pass a single contour to this
            cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255),1)


    #cv2.drawContours(frame, contours,-1,(255,0,0), 3)   # -1 for all


    #myObject = cv2.bitwise_and(frame, frame, mask=myMask)
    myObject1 = cv2.bitwise_and(frame, frame, mask=compositeMask)  
    #combined = cv2.bitwise_and(myMask, frame, mask=myMask)
    
   # myObjectSmall = cv2.resize(myObject, (int(width/2), int(height/2)))
    myMaskSmall = cv2.resize(compositeMask,(int(width), int(height)))
    #cv2.imshow('My Object', myObjectSmall)
    cv2.imshow('COM_Mask', compositeMask)
    
    myObjectSmall1 = cv2.resize(myObject1, (int(width), int(height)))
    #myMaskSmall1 = cv2.resize(myMask1,(int(width/2), int(height/2)))
    cv2.imshow('My Object1', myObjectSmall1)
   # cv2.imshow('myMask1', myMaskSmall1)

    


    #cv2.moveWindow('My Object', int(width/2), height)
    cv2.moveWindow('My Object1', width, height)
    cv2.moveWindow('COM_Mask', 0, height)

    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 