import cv2
from PIL import Image as Image

def convert_cv2_image_to_pill_image(image_opencv):
    # convert a cv2 image to a PIL image    

    # Notice the COLOR_BGR2RGB which means that the color is converted from BGR to RGB 
    color_coverted = cv2.cvtColor(image_opencv, cv2.COLOR_BGR2RGB) 

    image_pil = Image.fromarray(color_coverted) 

    return image_pil

def find_faces(img):
    
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )
    
    return faces