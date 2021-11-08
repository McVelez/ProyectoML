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

    #print(rects)
    #print()
    rectsList = rects.tolist()
    c = 0
    for rectangles in rectsList:
        sizeR = rectangles[2] * rectangles[3]
        rectsList[c].append(sizeR)
        c += 1
    rectsList.sort(key=lambda row: row[4], reverse=True) 
    rectsList = rectsList[:10]
    #print(rectsList)
    
    if len(rectsList) < 10:
        return

    minVal = rectsList[9][4]
    maxVal = rectsList[0][4]

    meanVal = 0
    for i in rectsList:
        meanVal += i[4]

    meanVal = meanVal / 10

    #print()
    rectsList.sort(key=lambda row: row[0], reverse=False)
    #print(rectsList)
    #print()

    

    # eliminate double letters 
    ignore = False
    if (maxVal / meanVal) > 1.5 and (minVal / meanVal) < 0.5:
        ignore = True
        print("DELETED")

    # quitar los ultimos 4 y primero caracteres del titulo (\ y .png)
    titulo = title
    letras = list(titulo)


    
    # TODO LO DEL FOLDER
    if ignore == False:
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
    #if(conte < 100):
    with open(image, 'rb') as file:
        nombre = image[15:-4] 
        path = image.title()
        print(nombre)
        processing(path, nombre)
        #conte += 1