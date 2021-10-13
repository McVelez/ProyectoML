from PIL import Image
import cv2
import glob

directory = glob.glob('CaptchaDataset/*.jpg')

# Funcion para procesar las imagenes
def processing(path, title):
    img = cv2.imread(path,0) # La imagen es convertida a una escala de blanco y negro
    ret, thresh2 = cv2.threshold(img,225,255,cv2.THRESH_BINARY_INV)
    imgPro = Image.fromarray(thresh2)
    imgPro.save(f"CaptchaDatasetCV2/{title}") # Se guarda la imagen procesada con el mismo titulo

# Iterar sobre las imagenes
for image in directory:
    with open(image, 'rb') as file:
        nombre = image.title() 
        nombre = nombre.removeprefix('Captchadataset')
        path = image.title()
        print(nombre)
        processing(path, nombre)
