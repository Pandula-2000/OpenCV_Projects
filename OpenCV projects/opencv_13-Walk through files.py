import os
import cv2
import face_recognition as FR


imgDir = "C:\\Users\pandu\Documents\Python\demoImages\known"

for root, dirs, files in os.walk(imgDir) :
    #print("my Working Folder  (root) is: ", root)
    #print("Directories in root: ", dirs)
    #print("my Files in root: ", files)

    for each in files:
        path = os.path.join(root, each)
        #name = each[:-4]   # Also works... But better to use the method below.(If we have different file formats, this method won't work).
        name = os.path.splitext(each)[0]
        print(name)
        img = FR.load_image_file(path)
        

#for i in os.walk(imgDir):
#   print(i)


