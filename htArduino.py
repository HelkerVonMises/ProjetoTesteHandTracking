import cv2
import math
import time
import HandTrackingModule as htm
from pyfirmata import Arduino

Mega = Arduino('COM4')

################################
wCam, hCam = 1080, 480  # Proporção: 1080, 480/640,480
################################

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)  # Webcam
cap.set(3, wCam)  # comprimento da imagem
cap.set(4, hCam)  # altura da imagem
detector = htm.handDetector()

detector = htm.handDetector(detectionCon=0.75)

dedosId = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()               # leitura da imagem
    img = detector.findHands(img)           # (img, draw=False) para tirar a marcação de detecção
    lmList = detector.findPosition(img)     # (img, draw=False) para tirar o circulo dos pontos de detecção

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        length = math.hypot(x2 - x1, y2 - y1)
        #  print(length)                           # 250, 40
        comp = int(length / 2)

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        # print(cx, cy)

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.circle(img, (cx, cy), comp, (255, 0, 0), 3)

        dedos = []

        if lmList[dedosId[0]][1] > lmList[dedosId[0] - 1][1]:
            dedos.append(1)
        else:
            dedos.append(0)

        for id in range(1, 5):
            if lmList[dedosId[id]][2] < lmList[dedosId[id] - 2][2]:
                dedos.append(1)
            else:
                dedos.append(0)
        totalDedos = dedos.count(1)

        print(totalDedos)

        if totalDedos == 1:
            Mega.digital[13].write(1)
            Mega.digital[12].write(0), Mega.digital[11].write(0), Mega.digital[10].write(0), Mega.digital[9].write(0)
        elif totalDedos == 2:
            Mega.digital[12].write(1), Mega.digital[13].write(1)
            Mega.digital[11].write(0), Mega.digital[10].write(0), Mega.digital[9].write(0)
        elif totalDedos == 3:
            Mega.digital[11].write(1), Mega.digital[12].write(1), Mega.digital[13].write(1)
            Mega.digital[10].write(0), Mega.digital[9].write(0)
        elif totalDedos == 4:
            Mega.digital[10].write(1), Mega.digital[12].write(1), Mega.digital[11].write(1), Mega.digital[13].write(1)
            Mega.digital[9].write(0)
        elif totalDedos == 5:
            Mega.digital[13].write(1), Mega.digital[12].write(1), Mega.digital[11].write(1)
            Mega.digital[10].write(1), Mega.digital[9].write(1)
        else:
            Mega.digital[13].write(0), Mega.digital[12].write(0), Mega.digital[11].write(0)
            Mega.digital[10].write(0), Mega.digital[9].write(0)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.imshow("image", img)
    cv2.waitKey(1)  # delay em ms

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
