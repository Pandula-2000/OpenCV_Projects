
from re import X
import cv2
import numpy as np

width = 640
height = 360
# 1920x1080
# 640x360
# 320x180
# 1280x720

evt = 0
x = 0
y = 0

def mouseClick(event, xPos, Ypos, flags, params):
    global evt
    global X
    global y
    if event == cv2.EVENT_LBUTTONDOWN :
        print(event)
        evt = event
        x = xPos
        y = Ypos
    if event==cv2.EVENT_RBUTTONUP:
        evt = event
        print(event)


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('cam1')
cv2.setMouseCallback('cam1', mouseClick)









while True:
    ignore, frame = cam.read()
   # hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

  # cv2.moveWindow('cam2',0,height)

    if evt == 1:
        r = np.zeros([250,250,3], dtype=np.uint8)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr = hsv[y][x]
        print(clr)
        #clr[0] = (clr[0]/180)*255
       # clr[1] = clr[1]/255
       # clr[2] = clr[2]/255
        #print(clr)
        r[:,:] = clr
        cv2.putText(r,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
        cv2.imshow('color', r)
        cv2.moveWindow('color', width,0)
        evt = 0   

    frame = cv2.flip(frame,1)
    
    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)
   # cv2.imshow('cam2',hsv)


    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 