# -*- coding: utf-8 -*-
"""
Created on Thurs Oct 07 21:40:18 2021
@author: Mạnh Thắng Hồ
"""

# import library
from imutils.perspective import four_point_transform
from imutils import contours
from skimage import io

import numpy as np
import argparse
import imutils
import cv2

#create global variable to store the path of input image
#if __name__ == "__main__":
#	img_path = './images/test_01.png'

#có thể truyền đường dẫn của ảnh vào trong lúc thực thi chương trình theo thư viện argparse của Python như sau:

# construct the argument parse and parse the arguments
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the input image")

args = vars(ap.parse_args())
if __name__ == "__main__":
    img_path = args["image"]
# define the answer key which maps the question number
# to the correct answer
image = img = io.imread(args["image"])
image=cv2.resize(image,(int(image.shape[0]/4),int(image.shape[1]/4)))
img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(5,5),1)
edged = cv2.Canny(img_blur, 1, 30)
cv2.imshow("Image after edged",edged)
#
thresh = cv2.threshold(edged, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
print(thresh.shape[0])

cv2.imshow("Result", thresh)

cv2.waitKey(0)