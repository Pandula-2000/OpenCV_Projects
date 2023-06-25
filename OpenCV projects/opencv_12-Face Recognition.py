import cv2
import face_recognition as FR    # Remember that FR works in RGB space
font = cv2.FONT_HERSHEY_SIMPLEX




donFace = FR.load_image_file("C:/Users/pandu/Documents/Python/demoImages/known/Donald Trump.jpg")
faceLoc = FR.face_locations(donFace)[0]
donFaceEncode = FR.face_encodings(donFace)[0]  # Train the model

nancyFace = FR.load_image_file("C:/Users/pandu/Documents/Python/demoImages/known/Nancy Pelosi.jpg")
faceLoc = FR.face_locations(nancyFace)[0]
nancyFaceEncode = FR.face_encodings(nancyFace)[0]

knownEncodings = [donFaceEncode, nancyFaceEncode]
names = ["Donald", "Nancy"]


unknownFace = FR.load_image_file("C:/Users/pandu/Documents/Python/demoImages/unknown/u3.jpg")
unknownFace_BGR = cv2.cvtColor(unknownFace, cv2.COLOR_RGB2BGR)
faceLocations = FR.face_locations(unknownFace)
unknownEncodings = FR.face_encodings(unknownFace,faceLocations)

for faceLocation, unknownEncoding in zip(faceLocations, unknownEncodings) :
    y1, x2, y2, x1 = faceLocation
    print(faceLocation)
    cv2.rectangle(unknownFace_BGR, (x1, y1), (x2,y2),(255,0,0),3)
    name = "unknown"
    matches = FR.compare_faces(knownEncodings, unknownEncoding)
    print(matches)



''' 
donFace_BGR = cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
print(faceLoc)
y1,x2,y2,x1 = faceLoc
cv2.rectangle(donFace_BGR,(x1,y1), (x2,y2), (255,0,0), 3)
cv2.imshow("My Window", donFace_BGR)
cv2.waitKey(5000)

'''

