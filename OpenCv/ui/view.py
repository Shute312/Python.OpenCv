#! C:\Python27\python.exe
# -*- coding: utf-8 -*-
__author__ = 'Shute'

from Tkinter import * 
import tkFileDialog
import numpy as np;
from PIL import Image
from PIL import ImageTk

class Track(object):
    def __init__(self,name,min,max,step,default):
        self.name = name
        self.key = name
        self.min = min
        self.max = max
        self.step = step
        self.default = default
        self.value = default

class View(Frame):
    def __init__(self,tk,size,tracks,inputs,changeCallback):
        '''
        @parma size:  type tuple
        @parma tracks:  type Track[]
        @parma inputs:  type tuple<name,value>[]
        '''
        Frame.__init__(self)
        self.size = size;
        self.tracks = [];
        self.inputs = [];
        self.controls = {};
        self.changeCallback = changeCallback;
        if(tracks!=None):
            if(isinstance(tracks,Track)):
                self.tracks.append(tracks);
            if(isinstance(tracks,list)):
                for i,item in enumerate(tracks):
                    self.tracks.append(item);

        if(inputs!=None):
            if(isinstance(inputs,list)):
                for i,item in enumerate(inputs):
                    self.inputs.append(item);
            else:
                self.inputs.append(inputs);


        self.place(in_=tk,rely = 0,relheight = 1,relwidth = 1);

        self.createWidgets()
        self.update()

    def createWidgets(self):
        usedHeight = 0;
        xPadding = 4
        yPadding = 4
        yOffset = yPadding;
        xOffset=xPadding;

        #TrackBar
        for i,item in enumerate(self.tracks):
            text = Label(self,text=item.name+":", font=("Arial",14));
            tk = Scale(self, from_=item.min, to=item.max,tickinterval = item.step,orient=HORIZONTAL, length=self.size[0]- xPadding*4-text.winfo_reqwidth()) #滑块
            tk.set(item.value);
            self.controls[item.name]=tk;
            yIncrement = max(text.winfo_reqheight(),tk.winfo_reqheight());
            text.place(x=xOffset,y=yOffset+(yIncrement-text.winfo_reqheight())/2);
            tk.place(x=xOffset+text.winfo_reqwidth()+xPadding,y=yOffset+(yIncrement-tk.winfo_reqheight())/2);
            yOffset = yOffset+yIncrement+yPadding;

        yIncrement = 0
        xOffset = xPadding
        #Input Box
        for i,item in enumerate(self.inputs):
            text = Label(self,text=item["name"]+":", font=("Arial",14));
            ip= Entry(self) #值输入
            ip.insert(0,item["value"]);
            self.controls[item["name"]]=ip;
            yIncrement = ip.winfo_reqheight();
            text.place(x=xOffset,y=yOffset)
            xOffset = xOffset+xPadding+text.winfo_reqwidth();
            ip.place(x=xOffset,y=yOffset)
            xOffset = xOffset+xPadding+ip.winfo_reqwidth();
       
        xOffset = xPadding;
        yOffset = yOffset + yIncrement + xPadding

        self.btnUpdate = Button(self, text='Update', command=self.update)
        self.btnUpdate.place(x=xOffset,y=yOffset)
        yOffset = yOffset + self.btnUpdate.winfo_reqheight()+yPadding;
        
        #Pictures
        self.srcImage = Label(image=None,bd=2)
        self.srcImage.place(x=xOffset,y=yOffset);
 
        # while the second panel will store the edge map
        self.dstImage = Label(image=None,bd=2)
        self.dstImage.place(x=(self.size[0]+xPadding)/2,y=yOffset);
        
    def setImage(self,ctrl,image):
        ctrl.configure(image=image)
        ctrl.image = image
        
    def setDst(self,image):
        self.dstImage.configure(image=image)
        self.dstImage.image = image

    def update(self):
        #获取控件的值
        params = {};
        for k,v in self.controls.iteritems():
            if isinstance(v,Scale):
                params[k] = v.get();
            elif isinstance(v,Entry):
                params[k] = v.get();

        (srcPath,dstPath) = self.changeCallback(params);
        self.setImage(self.srcImage,ImageTk.PhotoImage(Image.open(srcPath)));
        self.setImage(self.dstImage,ImageTk.PhotoImage(Image.open(dstPath)));
        