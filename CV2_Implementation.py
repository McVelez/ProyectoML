from PIL import Image
import cv2
import glob
from time import sleep
directory = glob.glob('CaptchaDataset/*.jpg')

# Funcion para procesar las imagenes
def processing(path, title):
    print(title)
    img = cv2.imread(path, 0) # La imagen es convertida a una escala de blanco y negro

    #image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
    #window_name = 'Image'
    # Displaying the image 

    
    cv2.imwrite("eje2.png", img)
    
    '''
    ret, thresh2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    imgPro = Image.fromarray(thresh2)
    imgPro.save("ejemplo.png")
    #imgPro.save(f"CaptchaDatasetCV2/{title}") # Se guarda la imagen procesada con el mismo titulo
    '''

'''
# Iterar sobre las imagenes
for image in directory:
    with open(image, 'rb') as file:
        nombre = image.title() 
        nombre = nombre.removeprefix('Captchadataset')
        path = image.title()
        print(nombre)
        processing(path, nombre)


'''

processing('00s6Q5Sfv7.jpg', '00s6Q5Sfv7')