
import cv2
import mediapipe as mp



width = 640
height = 360
# 1920x1080
# 640x360
# 320x180
# 1280x720

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))


hands = mp.solutions.hands.Hands(False,2,1,0.5,0.5)  # (is the frame static?, number of hands, 0/1, Some confidence values....)
mpDraw = mp.solutions.drawing_utils



while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame,1)
    frameRBG = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frameRBG)
    
    if results.multi_hand_landmarks != None :  # multi_hand.... is data for all the hands
        myHands = []
        for handLandMarks in results.multi_hand_landmarks:                                        # Step through 1 hand at a time.
            #print(handLandMarks)  
            myHand = []                                                                #  
            #mpDraw.draw_landmarks(frame, handLandMarks, mp.solutions.hands.HAND_CONNECTIONS)      # Draw one hand at a time.
            for Landmark in handLandMarks.landmark :   # Data for one hand
                data = (int(Landmark.x*width), int(Landmark.y*height))   # Scale x,y
                #print(data)
                myHand.append(data)   # Make a list that contains (x,y) positions of each 20 joints as tuples.
                #if len(myHand==20) :
            #print(len(myHand))
            myHands.append(myHand)
            cv2.circle(frame, myHand[19], 20, (255,0,255),-1)

        print(myHands)


    cv2.imshow('cam1', frame)
    cv2.moveWindow('cam1',0,0)
    
    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 