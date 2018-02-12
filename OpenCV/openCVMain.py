#coding: utf-8

from utils.utils import getTime
from PIL import Image
from pylab import *
import cv2


def test1():
    img = cv2.imread("F:/a.jpg")
    # cv2.namedWindow("Image")
    cv2.imshow("Image", img)
    cv2.waitKey(0)

def test2():
    im = Image.open("F:/a.jpg")  # 读取图片
    im.rotate(45).show()  # 将图片旋转，并用系统自带的图片工具显示图片
    # im = array(Image.open("F:/a.jpg"))
    # imshow(im)

print "start::", getTime()
# test1()
test2()

print "end::", getTime()