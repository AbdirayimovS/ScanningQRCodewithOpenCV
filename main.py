import cv2
import pyzbar.pyzbar as pyzbar


cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_PLAIN
color = (255,0,0)

while True:
    _, frame = cap.read()
    decodedObj = pyzbar.decode(frame)
    for obj in decodedObj:
        txt = obj.data
        txt = txt.decode("UTF-8") #to change from bytes class to string class

        x,y,w,h = obj.rect
        cv2.putText(frame, txt, (x, y), font, 2, color, 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)