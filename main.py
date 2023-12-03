from os.path import exists
import os

import cv2
from PIL import Image as Image



def convert(image_opencv):
    # Open image using openCV2 


    # Notice the COLOR_BGR2RGB which means that the color is 
    # converted from BGR to RGB 
    color_coverted = cv2.cvtColor(image_opencv, cv2.COLOR_BGR2RGB) 

    image_pil = Image.fromarray(color_coverted) 

    return image_pil


image_path = (input("Enter a path of image: "))

if not exists(image_path):
    print("This path doesn't exist.")
    exit(1)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'roblox face.png')
roblox_face_path = (filename)

img = cv2.imread(image_path)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)



faces = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

image_pil = convert(img)
for face in faces:
    x, y, w, h =  face

    roblox_face = Image.open(roblox_face_path)

    roblox_face =roblox_face.resize((w,h))
    roblox_face_map = roblox_face.load()
    image_map = image_pil.load()
    b=0
    for j in range(y,y+w):
        a= 0 
        for i in range(x,x+w):
        
            image_map[i,j] = roblox_face_map[a,b]
            
           
            a+=1
        b+=1

image_pil.show()