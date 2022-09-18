#------------@Copyright 2022 All Rights Reserved by VK ---------------

import cv2
import pandas as pd
import matplotlib.pyplot as plt


#Set the Path of haarcascade_frontalface_alt.xml Here Before Run...
face_cascade = cv2.CascadeClassifier("Before run set path here")

#-----------DON'T CHANGE ANYTHING HERE-----------------------

def detect_faces(img):
    faces = face_cascade.detectMultiScale(img)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    plt.imshow(img)
    plt.show()

image = cv2.imread(input("Enter The Image Name with Extension Correctly ?\n"))
detect_faces(image)

#----------------github.com/vickyspace------------------


