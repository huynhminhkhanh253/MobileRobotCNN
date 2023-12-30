import cv2
cap = cv2.VideoCapture(0)

def detect(img):
    v=0
    stopcascade = cv2.CascadeClassifier('/home/pi/Desktop/MainProject/stop_sign.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    stop = stopcascade.detectMultiScale(imgGray, 1.2, 8)
    for (x, y, w, h) in stop:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        v = y + h
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        print(v)
    return v
while True:
    _, img = cap.read()
    detect(img)
    cv2.imshow("output",img)
    cv2.waitKey(1)