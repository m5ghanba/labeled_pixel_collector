# Collecting labeled data          Mohsen Ghanbari May 2020

# Purpose: In this updated version, the user only needs to doubleclick the points for each class and close the window
# when they are done with each class.
# Input: 1) number of ground truth classes, t_num_cls  2) an image of the scene, im
# Output: a csv file containing the labels and coordinates (top right being (1,1)), labels
import numpy as np
import imageio
import matplotlib.pyplot as plt
import csv
import os
import cmath
import cv2
from tkinter import Tk
from tkinter.filedialog import askdirectory


p_directory = askdirectory(title='Select Folder') # shows dialog box and return the path
p_directory = p_directory + "/"

t_num_cls = int (input("Input the number of ground truth classes: "))


#This variable we use to store the pixel location
refPt = []
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,",",y)
        refPt.append([x, y])


im = imageio.imread(p_directory + 'image_for_labeling.png')
h = im.shape[0]
w = im.shape[1]

label_directory = 'labeled data'
path = os.path.join(p_directory, label_directory)
if(not os.path.isdir(path)):
   os.mkdir(path)

with open(path + '/labels.csv', mode='w', newline='') as label_file:
    writer = csv.writer(label_file)
    for cl in range (1, t_num_cls + 1):
        print("collecting labeled pixels for class ", cl)
        permit = input("Continue? (If yes, press y)")
        if permit == "y":
            #for pix in range (0, t_num_labele_pixs):

            img = cv2.imread(p_directory + "image_for_labeling.png")
            scale_width = 640 / img.shape[1]
            scale_height = 480 / img.shape[0]
            scale = min(scale_width, scale_height)
            window_width = int(img.shape[1] * scale)
            window_height = int(img.shape[0] * scale)
            cv2.namedWindow("image", cv2.WINDOW_NORMAL)
            cv2.resizeWindow('image', window_width, window_height)
            cv2.imshow("image", img)
            # calling the mouse click event
            cv2.setMouseCallback("image", click_event)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


            for item in refPt:
                writer.writerow([str(cl), item[0]+1, item[1]+1])
            refPt.clear()



