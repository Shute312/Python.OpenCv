import cv2;
import numpy;
import math;

img = cv2.imread('images//book1.jpg')
height,width = img.shape[:2]
math.sin(30);
H = numpy.float32([[1,-0.7071067811865475,width*0.7],[0,1,0]])
dst = cv2.warpAffine(img,H,(width*2,height))

cv2.imshow('Affine',dst)   

cv2.waitKey();
cv2.destroyAllWindows()