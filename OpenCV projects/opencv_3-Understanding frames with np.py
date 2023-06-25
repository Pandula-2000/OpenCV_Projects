

import numpy as np
import cv2


while True :
   # frame = np.zeros([250,250],dtype=np.uint8)        # Grey scale frame
    frame_BGR= np.zeros([1000,1000,3],dtype=np.uint8)    # Color frame

    frame_BGR[:] = (0,255,0)      # RED Box

    #cv2.imshow("The_FRAME1",frame)                    # Grey scale frame
    cv2.imshow("The_FRAME2",frame_BGR)                 # Color frame
    if cv2.waitKey(1)&0xff == ord('q') :
        break



