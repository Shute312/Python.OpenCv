# -*- coding: utf-8 -*-
import os;
import sys;

def getAbsPath(path):
    file = sys.argv[0];#main file path
    if path is None or len(path) ==0 :
        return file;
    original = path;
    root = sys.path[0];
    dir = root;
    if path.startswith("\\"):
        return dir + path;
    else:
        while path.startswith("..\\"):
            dir = os.path.dirname(dir);
            path = path[3:]
        return dir +"\\"+ path;