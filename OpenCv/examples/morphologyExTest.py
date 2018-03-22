#! C:\Python27\python.exe
# -*- coding: utf-8 -*-

__author__ = 'Shute'
from ui.view import *;
import cv2;

tracks = [Track("ksize.x",1,25,1,5),Track("ksize.y",1,25,1,5)]
selects = [Select("Pattern",("MORPH_CLOSE","MORPH_OPEN","MORPH_GRADIENT","MORPH_TOPHAT","MORPH_BLACKHAT"))]

size = (1000,800)

srcPath="images\\pepper.jpg";
img = cv2.imread(srcPath,1);
dstPath = "temp\\temp.jpg"

def update(parmas):
    patternStr = parmas["Pattern"];
    patternValue = cv2.MORPH_CLOSE;
    if patternStr == "MORPH_OPEN":
        patternValue = cv2.MORPH_OPEN
    elif patternStr == "MORPH_CLOSE":
        patternValue = cv2.MORPH_CLOSE
    elif patternStr == "MORPH_GRADIENT":
        patternValue = cv2.MORPH_GRADIENT
    elif patternStr == "MORPH_TOPHAT":
        patternValue = cv2.MORPH_TOPHAT
    elif patternStr == "MORPH_BLACKHAT":
        patternValue = cv2.MORPH_BLACKHAT

    element = cv2.getStructuringElement(cv2.MORPH_RECT,(parmas["ksize.x"],parmas["ksize.y"]));
    dst = cv2.morphologyEx(img,patternValue, element);
    cv2.imwrite(dstPath,dst);
    return (srcPath,dstPath);

tk = Tk();
tk.geometry("{0}x{1}".format(size[0],size[1]));
view = View(update,tk,size,tracks,None,selects)
# 设置窗口标题:
tk.title('morphologyEx')
# 主消息循环:
tk.mainloop()
