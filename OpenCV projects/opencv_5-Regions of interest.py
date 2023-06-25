from turtle import width
import cv2

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

    frameROI = frame[150:210,250:390]
    frameROI_Grey = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)      # Make a grey frame
    frameROI_BGR = cv2.cvtColor(frameROI_Grey,cv2.COLOR_GRAY2BGR)
    frame[:60,:140] = (0,0,0)                 #frameROI_BGR
    cv2.imshow("My_ROI",frameROI)
    cv2.imshow("My_ROI_GRAY",frameROI_Grey)
    cv2.moveWindow("My_ROI",650,0)
    cv2.moveWindow("My_ROI_GRAY",650,110)
    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)

    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 