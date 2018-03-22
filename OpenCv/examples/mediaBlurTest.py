#! C:\Python27\python.exe
# -*- coding: utf-8 -*-

__author__ = 'Shute'
from ui.view import *;
import cv2;

tracks = [Track("ksize.x",1,25,2,1),Track("ksize.y",1,25,2,1)]

size = (1000,800)

srcPath="images\\pepper.jpg";
img = cv2.imread(srcPath,1);
dstPath = "temp\\temp.jpg"

def update(parmas):
    dst = cv2.blur(img,(parmas["ksize.x"],parmas["ksize.y"]));
    cv2.imwrite(dstPath,dst);
    return (srcPath,dstPath);

tk = Tk();
tk.geometry("{0}x{1}".format(size[0],size[1]));
view = View(update,tk,size,tracks,None,None)
# 设置窗口标题:
tk.title('MedianBlur')
# 主消息循环:
tk.mainloop()
