from PIL import Image
import glob

# Folder en donde se encuentra el dataset de imagenes de CAPTCHAS
directory = glob.glob('CaptchaDataset/*.jpg')

# Funcion para procesar las imagenes
def processing(img, title):
    img = Image.open(file).convert('L') # La imagen es convertida a una escala de blanco y negro
    imgProcessed = Image.eval(img, (lambda a: 255 if a <= 225 else 0)) # Se enfatizan solamente los colores negros y blancos
    imgProcessed.save(f"CaptchaDatasetProcessed/{title}") # Se guarda la imagen procesada con el mismo titulo

# Iterar sobre las imagenes
for image in directory:
    with open(image, 'rb') as file:
        nombre = image.title() 
        nombre = nombre.removeprefix('Captchadataset')
        print(nombre)
        processing(file, nombre)