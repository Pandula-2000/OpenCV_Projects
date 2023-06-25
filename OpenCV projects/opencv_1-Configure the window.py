import cv2
# print(cv2.__version__)

cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("CAM1", grayFrame)    # Move the frame to a pre specified place
    cv2.imshow("CAM2", frame)
    #cv2.imshow("CAM3", grayFrame)
    #cv2.imshow("CAM4", frame)
    cv2.moveWindow('CAM1',640,300)
    cv2.moveWindow('CAM2',0,0)
   # cv2.moveWindow('my WEB CAM',0,0)
   # cv2.moveWindow('my WEB CAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()