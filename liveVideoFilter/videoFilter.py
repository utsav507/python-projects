# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 08:10:24 2019

@author: Salman Ahmad
"This program will capture live video and apply filters to that video"""

import cv2
video=cv2.VideoCapture(0)
while True:
    check, frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video Capturing and Filtering!",gray)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    
video.release()
cv2.destroyAllWindows