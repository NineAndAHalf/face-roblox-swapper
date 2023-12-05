from os.path import exists
import os

from functions import *

import cv2
from PIL import Image as Image


image_path = input("Enter a path of image: ")

if not exists(image_path):
    print("This path doesn't exist.")
    exit(1)

cut_backround  = True if input().lower() == 'y' else False 

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'roblox face.png')
roblox_face_path = (filename)

img = cv2.imread(image_path)

faces = find_faces(img)
roblox_face = Image.open(roblox_face_path)

image_pil = convert_cv2_image_to_pill_image(img)
for face in faces:
    face_x_position, face_y_position, face_width, face_height =  face    

    roblox_face =roblox_face.resize((face_width,face_height))
    roblox_face_map = roblox_face.load()
    image_map = image_pil.load()
    a=0
    for j in range(face_y_position,face_y_position+face_width):
        b= 0 
        for i in range(face_x_position,face_x_position+face_width):
            if cut_backround:
                if roblox_face_map[b,a] != roblox_face_map[0,0]:
                    image_map[i,j] = roblox_face_map[b,a]
            else:
                image_map[i,j] = roblox_face_map[b,a]
            b+=1
            
        a+=1

image_pil.show()