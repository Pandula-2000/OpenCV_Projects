

import numpy
import cv2

width = 640
height = 360
# 1920x1080
# 640x360
# 320x180
# 1280x720

upper_left = (420,180)
lower_right = (500,260)
my_radius = 30
my_thickness = 3
font_size = 1
my_font = cv2.FONT_HERSHEY_COMPLEX
my_text = "Adelee"

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()

    # frame[140:220,250:390] = (0,0,55)              # You can do this but there are better ways with CV2

    cv2.rectangle(frame, upper_left, lower_right, (0,255,255), -1)    # -1 for fill rect
    
    cv2.circle(frame, (int(width/2),int(height/2)), my_radius,(255,0,0),-1)
    cv2.putText(frame,my_text,(150,50), my_font, font_size, (255,0,0), my_thickness)
   
    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)

    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()    


