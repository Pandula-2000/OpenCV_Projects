
import codecs
import cv2
import numpy as np
from pyzbar.pyzbar import decode

width = 360*2
height = 180*2
# 1920x1080
# 640x360
# 320x180
# 1280x720

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame,1)

    
    codes = decode(frame)
    

    for code in codes :
        data = code.data.decode("utf-8")
        #print(code.data)
        pts = np.array([code.polygon], np.int32).reshape(-1,1,2)
        
        cv2.polylines(frame,[pts],True,(0,0,255),4)

    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)



    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 