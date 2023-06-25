import cv2

width = 640
height = 360
xPos = int(width/2)
yPos = int(height/2)
myradius = 10

# 1920x1080
# 640x360
# 320x180
# 1280x720

def myCallBack1(val) :
    global xPos
    xPos = val
    print("X_val: ", val)
def myCallBack2(val) :
    global yPos
    yPos = val
    print("Y_val: ", val)

def myCallBack3(val) :
    global myradius
    myradius = val
    print("Radius: ", val)



cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

"""
cv2.namedWindow("My_Trackbarx")
cv2.resizeWindow("My_Trackbarx",400,100)
cv2.moveWindow("My_Trackbarx",width,0)

"""

cv2.namedWindow("My_Trackbars")
cv2.resizeWindow("My_Trackbars",400,150)
cv2.moveWindow("My_Trackbars",width,0)

cv2.createTrackbar("xPos","My_Trackbars",xPos,width,myCallBack1)   # Max 1920
                                                              # Start value is which value tracker is set at the begininning (initial)
                                                              # You cant set an minimum value. It is zero by default
cv2.createTrackbar("yPos","My_Trackbars",yPos,height,myCallBack2) 
cv2.createTrackbar("Radius","My_Trackbars",myradius,int(height/2),myCallBack3)

while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.circle(frame,(xPos,yPos),myradius,(255,0,0),-1 )

    cv2.imshow('cam1',frame)
    cv2.moveWindow('cam1',0,0)

    if cv2.waitKey(1) & 0xff == ord('q') :
        break

cam.release()                 