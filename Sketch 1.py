import cv2
import time
import HandTrackingModule as htm

################################
wCam, hCam = 640, 480  # 1080, 480         640,480
################################

pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
    cv2.rectangle(img, (120, 40), (520, 440), (255, 0, 0), 1)
    cv2.rectangle(img, (253, 40), (387, 440), (255, 0, 0), 1)
    cv2.rectangle(img, (120, 170), (520, 310), (255, 0, 0), 1)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]  # thumb coordinate
        x2, y2 = lmList[8][1], lmList[8][2]  # indicator coordinate
        # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.putText(img, f'x1: {int(x1)}', (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv2.putText(img, f'y1: {int(y1)}', (10, 130), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv2.putText(img, f'x2: {int(x2)}', (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.putText(img, f'y2: {int(y2)}', (10, 190), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

        if 120 <= lmList[8][1] <= 253 and 40 <= lmList[8][2] <= 173:        # Quadrante 01
            cv2.putText(img, 'Indicador: 1', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 253 <= lmList[8][1] <= 387 and 40 <= lmList[8][2] <= 173:      # Quadrante 02
            cv2.putText(img, 'Indicador: 2', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 387 <= lmList[8][1] <= 520 and 40 <= lmList[8][2] <= 173:      # Quadrante 03
            cv2.putText(img, 'Indicador: 3', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 120 <= lmList[8][1] <= 253 and 173 <= lmList[8][2] <= 310:     # Quadrante 04
            cv2.putText(img, 'Indicador: 4', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 253 <= lmList[8][1] <= 387 and 173 <= lmList[8][2] <= 310:     # Quadrante 05
            cv2.putText(img, 'Indicador: 5', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 387 <= lmList[8][1] <= 520 and 173 <= lmList[8][2] <= 310:     # Quadrante 06
            cv2.putText(img, 'Indicador: 6', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 120 <= lmList[8][1] <= 253 and 310 <= lmList[8][2] <= 440:     # Quadrante 07
            cv2.putText(img, 'Indicador: 7', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 253 <= lmList[8][1] <= 387 and 310 <= lmList[8][2] <= 440:     # Quadrante 08
            cv2.putText(img, 'Indicador: 8', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 387 <= lmList[8][1] <= 540 and 310 <= lmList[8][2] <= 440:     # Quadrante 09
            cv2.putText(img, 'Indicador: 9', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        else:
            cv2.putText(img, 'Indicador: 0', (120, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)

        if 120 <= lmList[12][1] <= 253 and 40 <= lmList[12][2] <= 173:
            cv2.putText(img, 'Medio: 1', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 253 <= lmList[12][1] <= 387 and 40 <= lmList[12][2] <= 173:
            cv2.putText(img, 'Medio: 2', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 387 <= lmList[12][1] <= 520 and 40 <= lmList[12][2] <= 173:
            cv2.putText(img, 'Medio: 3', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 120 <= lmList[12][1] <= 253 and 173 <= lmList[12][2] <= 310:
            cv2.putText(img, 'Medio: 4', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 253 <= lmList[12][1] <= 387 and 173 <= lmList[12][2] <= 310:
            cv2.putText(img, 'Medio: 5', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 387 <= lmList[12][1] <= 520 and 173 <= lmList[12][2] <= 310:
            cv2.putText(img, 'Medio: 6', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 120 <= lmList[12][1] <= 253 and 310 <= lmList[12][2] <= 440:
            cv2.putText(img, 'Medio: 7', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 253 <= lmList[12][1] <= 387 and 310 <= lmList[12][2] <= 440:
            cv2.putText(img, 'Medio: 8', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        elif 387 <= lmList[12][1] <= 540 and 310 <= lmList[12][2] <= 440:
            cv2.putText(img, 'Medio: 9', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)
        else:
            cv2.putText(img, 'Medio: 0', (387, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 1)

    cv2.imshow("image", img)
    cv2.waitKey(1)
