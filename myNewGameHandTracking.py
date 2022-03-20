import cv2
import time
import HandTrackingModule as htm

################################
wCam, hCam = 640, 480          # 1080, 480         640,480
################################

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)               # (img, draw=False) para tirar a marcação de detecção
    lmList = detector.findPosition(img)         # (img, draw=False) para tirar o circulo dos pontos de detecção
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)
