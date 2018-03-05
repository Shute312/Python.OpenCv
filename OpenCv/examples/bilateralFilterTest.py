#! C:\Python27\python.exe
# -*- coding: utf-8 -*-

__author__ = 'Shute'
from ui.view import *;
import cv2;

tracks = [Track("d",1,100,2,25),Track("sigmaColor",1,100,2,50),Track("sigmaSpace",1,100,2,12)]

size = (1000,800)

srcPath="images\\pepper.jpg";
img = cv2.imread(srcPath,1);
dstPath = "temp\\temp.jpg"

def update(parmas):
    dst =  cv2.bilateralFilter(img,25,25*2,25/2)
    cv2.imwrite(dstPath,dst);
    return (srcPath,dstPath);

tk = Tk();
tk.geometry("{0}x{1}".format(size[0],size[1]));
view = View(tk,size,tracks,None,update)
# 设置窗口标题:
tk.title('BilateralFilter')
# 主消息循环:
tk.mainloop()
