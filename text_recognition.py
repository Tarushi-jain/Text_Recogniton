import cv2
import easyocr
from matplotlib import pyplot as plt 
import numpy as np

Image_Path=input("Enter the image path or file name :")
img = cv2.imread(Image_Path)
reader = easyocr.Reader(['en'],gpu=False)
result=reader.readtext(Image_Path)
print(result)

top_left=tuple(result[0][0][0])
bottom_right=tuple(result[0][0][2])
text=result[0][1]
font=cv2.FONT_HERSHEY_SIMPLEX


img=cv2.imread(Image_Path)
for detection in result:
    top_left=tuple((int(val) for val in detection[0][0]))
    bottom_right=tuple((int(val) for val in detection[0][2]))
    text = detection[1]
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.rectangle(img,top_left,bottom_right,(0,255,0),5)
    img=cv2.putText(img,text,top_left,font,2,(255,255,255),2,cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()