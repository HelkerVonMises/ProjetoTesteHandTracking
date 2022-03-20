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

        if 120 <= lmList[8][1] <= 253 and 40 <= lmList[8][2] <= 173:
            cv2.putText(img, '1', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 253 <= lmList[8][1] <= 387 and 40 <= lmList[8][2] <= 173:
            cv2.putText(img, '2', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 387 <= lmList[8][1] <= 520 and 40 <= lmList[8][2] <= 173:
            cv2.putText(img, '3', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 120 <= lmList[8][1] <= 253 and 173 <= lmList[8][2] <= 310:
            cv2.putText(img, '4', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 253 <= lmList[8][1] <= 387 and 173 <= lmList[8][2] <= 310:
            cv2.putText(img, '5', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 387 <= lmList[8][1] <= 520 and 173 <= lmList[8][2] <= 310:
            cv2.putText(img, '6', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 120 <= lmList[8][1] <= 253 and 310 <= lmList[8][2] <= 440:
            cv2.putText(img, '7', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 253 <= lmList[8][1] <= 387 and 310 <= lmList[8][2] <= 440:
            cv2.putText(img, '8', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        elif 387 <= lmList[8][1] <= 540 and 310 <= lmList[8][2] <= 440:
            cv2.putText(img, '9', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)
        else:
            cv2.putText(img, '0', (100, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0), 2)

        if 120 <= lmList[12][1] <= 253 and 40 <= lmList[12][2] <= 173:
            cv2.putText(img, '1', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 253 <= lmList[12][1] <= 387 and 40 <= lmList[12][2] <= 173:
            cv2.putText(img, '2', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 387 <= lmList[12][1] <= 520 and 40 <= lmList[12][2] <= 173:
            cv2.putText(img, '3', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 120 <= lmList[12][1] <= 253 and 173 <= lmList[12][2] <= 310:
            cv2.putText(img, '4', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 253 <= lmList[12][1] <= 387 and 173 <= lmList[12][2] <= 310:
            cv2.putText(img, '5', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 387 <= lmList[12][1] <= 520 and 173 <= lmList[12][2] <= 310:
            cv2.putText(img, '6', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 120 <= lmList[12][1] <= 253 and 310 <= lmList[12][2] <= 440:
            cv2.putText(img, '7', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 253 <= lmList[12][1] <= 387 and 310 <= lmList[12][2] <= 440:
            cv2.putText(img, '8', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        elif 387 <= lmList[12][1] <= 540 and 310 <= lmList[12][2] <= 440:
            cv2.putText(img, '9', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        else:
            cv2.putText(img, '0', (150, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    cv2.imshow("image", img)
    cv2.waitKey(1)
