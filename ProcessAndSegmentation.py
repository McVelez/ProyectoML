import cv2
from PIL import Image
import glob
import os
import numpy as np 

def processing(path, title):
    # Dimensiones por modificar
    width = 40
    height = 40

    img = cv2.imread(path,0)

    (h, w) = img.shape[:2]
    image_size = h*w
    mser = cv2.MSER_create()
    mser.setMaxArea(round(image_size/2))
    mser.setMinArea(10)

    #ret, thresh2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
    ret, thresh2 = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
    regions, rects = mser.detectRegions(thresh2)

    print(rects)
    print()
    rectsList = rects.tolist()
    c = 0
    for rectangles in rectsList:
        sizeR = rectangles[2] * rectangles[3]
        rectsList[c].append(sizeR)
        c += 1
    rectsList.sort(key=lambda row: row[4], reverse=True) 
    rectsList = rectsList[:10]
    print(rectsList)
    print()
    rectsList.sort(key=lambda row: row[0], reverse=False)
    print(rectsList)
    print()

    
    # quitar los ultimos 4 y primero caracteres del titulo (\ y .png)
    titulo = title[1:-4]
    letras = list(titulo)

    # TODO LO DEL FOLDER
    path = "CAPTCHAS_SEGMENTADOS/" + titulo
    os.mkdir(path)
    
    cont = 0
    for x,y,w,h,s in rectsList:
        imgPro = Image.fromarray(thresh2[y:y+h,x:x+w])
        imgPro = imgPro.resize((width, height), Image.ANTIALIAS)
        imgPro.save("CAPTCHAS_SEGMENTADOS/" + str(titulo) + "/{}".format(str(cont) + '_' + letras[cont] + '.PNG'))
        cont+=1
    

directory = glob.glob('CaptchaDataset/*.jpg')
conte = 0
for image in directory:
    if(conte < 1):
        conte += 1
        with open(image, 'rb') as file:
            nombre = image.title() 
            nombre = nombre.removeprefix('Captchadataset')
            path = image.title()
            print(nombre)
            processing(path, nombre)
