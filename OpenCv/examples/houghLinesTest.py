#! C:\Python27\python.exe
# -*- coding: utf-8 -*-
__author__ = 'Shute'

import numpy as np;
import cv2;
import random;
from ui.view import *;
from utils.matUtils import *;

size = (1200,900)
srcPath="images\\book1.jpg";
img = cv2.imread(srcPath,1);
blockSize = getCol(img)/64;
C=getCol(img)/25;
minLineLength = getCol(img)*2/5;
maxLineGap = getCol(img)/8;
threshold = getCol(img)/25;
tracks = [Track("blockSize",1,100,2,blockSize),Track("C",1,100,2,C),Track("threshold",4,200,4,threshold),Track("minLineLength",10,1000,20,minLineLength),Track("maxLineGap",1,200,5,maxLineGap)]

dstPath1 = "temp/temp1.jpg"
dstPath2 = "temp/temp2.jpg"

def update(parmas):
    gray = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY);
    blockSize = parmas["blockSize"];
    if blockSize%2==0:
        blockSize+=1;
    if blockSize<3:
        blockSize=3;
    binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,blockSize,parmas["C"])
    #binary = cv2.threshold(gray,0,255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV);
    cv2.imwrite(dstPath1,binary);#输出二值图
    rho = 1;#距离分辨率，一般为1
    theta =  np.pi / 180;#为角度的分辨率，一般CV_PI/180
    lines = cv2.HoughLinesP(image = binary, rho = rho,theta = theta,threshold=parmas["threshold"],minLineLength = parmas["minLineLength"],maxLineGap = parmas["maxLineGap"]);
    dst = img.copy();
    if type(lines) !=NoneType:
        for i in lines:
            line=i.T;
            cv2.line(dst,(line[0],line[1]),(line[2],line[3]),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),1);
    
    cv2.imwrite(dstPath2,dst);

    #输出2个路径，一个是二值化后的图片，一个是霍夫线
    return (dstPath1,dstPath2);

tk = Tk();
tk.geometry("{0}x{1}".format(size[0],size[1]));
view = View(update,tk,size,tracks,None,None)
# 设置窗口标题:
tk.title('Test')
# 主消息循环:
tk.mainloop()
