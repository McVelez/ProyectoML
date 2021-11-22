import cv2
from PIL import Image
import glob
import os
import numpy as np 

def processing(path, title):
    # Dimensiones por modificar
    width = 40
    height = 40  

    # Se hace una lectura de la imagen
    img = cv2.imread(path,0)

    # Variables para identificar los caracteres por bloques (islas) para realizar la segmentacion
    (h, w) = img.shape[:2]
    image_size = h*w
    mser = cv2.MSER_create()
    mser.setMaxArea(round(image_size/2))
    mser.setMinArea(10)

    # Preprocesamiento para convertir la imagen en binario (blanco y negro)
    ret, thresh2 = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
    
    # Identificacion de rectangulos y regiones (para segmentar los caracteres)
    regions, rects = mser.detectRegions(thresh2)

    # Calcular el area de los rectangulos identificados y obtener unicamente los 10 bloques mas grandes (los rects de las letras)
    rectsList = rects.tolist()
    c = 0
    for rectangles in rectsList:
        sizeR = rectangles[2] * rectangles[3]
        rectsList[c].append(sizeR)
        c += 1
    rectsList.sort(key=lambda row: row[4], reverse=True) 
    rectsList = rectsList[:10]
   
    # En caso de que solamente se hayan identificado menos de 10 bloques descartar dicha imagen
    if len(rectsList) < 10:
        return

    # Valores de gestion para identificar si una imagen es necesario de descartar (Puede que algunos bloques sean insignificativos, es decir, el bloque representa una parte interna de un caracter y no del caracter completo como tal)
    minVal = rectsList[9][4]
    maxVal = rectsList[0][4]
    meanVal = 0
    for i in rectsList:
        meanVal += i[4]
    meanVal = meanVal / 10

    # Ordenamiento de los rectangulos en base a sus posiciones en x (Para guardar las letras de forma secuencial para solucionar el CAPTCHA)
    rectsList.sort(key=lambda row: row[0], reverse=False)
    
    # En caso de que se identifique un bloque insignificativo se descarta dicho Captcha 
    ignore = False
    if (maxVal / meanVal) > 1.5 and (minVal / meanVal) < 0.5:
        ignore = True
        print("DELETED")

    # Variables para asignar el nombre de la carpeta que contiene las letras segmentadas
    titulo = title
    letras = list(titulo)

    # En caso de que la imagen haya sido segmentada y preprocesada correctamente se almacenan
    if ignore == False:
        # Crear un folder especifico para el captcha segmentado
        path = "CAPTCHAS_SEGMENTADOS/" + titulo
        os.mkdir(path)
        
        cont = 0
        for x,y,w,h,s in rectsList:
            # En base a la informacion de los rectangulos identificados se guardan las imagenes en base a las dimensiones y posiciones descritas por el rectangulo
            imgPro = Image.fromarray(thresh2[y:y+h,x:x+w])
            imgPro = imgPro.resize((width, height), Image.ANTIALIAS)
            
            # Se guarda la imagen en el folder de CAPTCHAS_SEGMENTADOS con un formato numerico para asegurar la integridad de orden de los caracteres
            imgPro.save("CAPTCHAS_SEGMENTADOS/" + str(titulo) + "/{}".format(str(cont) + '_' + letras[cont] + '.PNG'))
            cont+=1
    
# Directorio en donde se encuentra el Dataset utilizado
directory = glob.glob('CaptchaDataset/*.jpg')

# Iterar sobre todas las imagenes para preprocesarlas y segmentarlas
for image in directory:
    with open(image, 'rb') as file:
        nombre = image[15:-4] 
        path = image.title()
        print(nombre)
        processing(path, nombre)