from __future__ import print_function
import cv2 as cv
import argparse

backSub = cv.createBackgroundSubtractorKNN(detectShadows=True)

cap = cv.VideoCapture(0) # video capture source camera (Here webcam of laptop)
ret,ref_frame = cap.read()

if not cap.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    fgMask = backSub.apply(frame)

    cv.rectangle(frame, (10, 2), (100, 20), (255, 255, 255), -1)
    cv.putText(frame, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break