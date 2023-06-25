
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

while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 