import cv2
import mediapipe as mp
import time
import numpy as np
import HandTrackingModule as htm
import math

################################
wCam, hCam = 1080, 480  # 1080, 480         640,480
################################

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector()

detector = htm.handDetector(detectionCon=0.7)

dedosId = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)  # (img, draw=False) para tirar a marcação de detecção
    lmList = detector.findPosition(img)  # (img, draw=False) para tirar o circulo dos pontos de detecção

    cv2.rectangle(img, (50, 130), (100, 430), (0, 255, 0), 3)

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        length = math.hypot(x2 - x1, y2 - y1)
        # print(length)                           # 250, 40
        comp = int(length/2)

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        # print(cx, cy)

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.circle(img, (cx, cy), comp, (0, 255, 0), 3)

        dedos = []

        for id in range(0, 5):
            if lmList[dedosId[id]][2] < lmList[dedosId[id]-2][2]:
                dedos.append(1)
            else:
                dedos.append(0)
        print(dedos)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)
