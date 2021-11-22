import os
import torch
from torch.utils.data import Dataset
import pandas as pd
import cv2

class CaracterDataset(Dataset):

    # Inicializacion de variables
    def __init__(self, annotations_file, image_dir, device, individual=True):
        # Variable que contiene la metadata e información relevante para cada archivo de imagen preprocesado y segmentado
        self.annotations = pd.read_csv(annotations_file) 
        # Directorio en donde se tienen todas las carpetas e imagenes segmentadas y preprocesadas
        self.image_dir = image_dir 
        # Dispositivo por ser asignado en caso de tener CUDA disponible
        self.device = device
        # Variable para determinar si se esta utilizando solamente los archivos individuales o como conjuntos
        self.individual = individual

    # Para identificar la cantidad de archivos en el dataset
    def __len__(self):
        return len(self.annotations)

    # GetItem para acceder a items del dataset
    def __getitem__(self, index):
        # Obtener el path y etiqueta del archivo de cada imagen
        image_sample_path = self._get_image_sample_path(index) 
        label = self._get_image_sample_label(index)

        # Realizar una lectura de la imagen y transformarla a un tensor object (para poder utilizar el modelo implementado)
        img = cv2.imread(image_sample_path)
        img = torch.from_numpy(img)
        img = torch.Tensor.float(img)

        # Se asigna la informacion de cada imagen al dispositivo disponible (En caso de tener CUDA el procesamiento es mas rapido)
        img = img.to(self.device)

        # Reducir la imagen a un solo canal (normalizacion)
        img = self._mix_down_if_necessary(img) 

        # Regresar como salida la imagen (tensor object) y su etiqueta correspondiente (string)
        return img, label

    # Funcion para normalizar todas las imagenes a un solo canal
    def _mix_down_if_necessary(self, img):
        # Si el canal de la imagen es mayor a uno entonces se realiza una normalizacion a un solo canal por medio de torch.mean
        if img.shape[0] > 1: 
            img = torch.mean(img, dim=0, keepdim=True)
        return img

    # Funcion para obtener la direccion completa de cada imagen
    def _get_image_sample_path(self, index):
        # Obtener la direccion del folder y del archivo en base a la informacion almacenada en el archivo csv
        if self.individual:
            fold = f"fold{self.annotations.iloc[index, 2]}" 
        else:
            # En caso de usar el CAPTCHA_VALIDACION por ejemplo (en donde es necesario considerar conjuntos de archivos)
            fold = self.annotations.iloc[index, 2]
        
        filename = self.annotations.iloc[index, 3]

        # Unir los paths del folder y del nombre del archivo para obtener la dirección completa, para asi poder acceder adecuadamente a todos los archivos almacenados
        path = os.path.join(self.image_dir, fold, filename)

        # Regresar la direccion completa en donde se encuentra cada imagen
        return path

    # Funcion para obtener la etiqueta correspondiente a cada archivo de imagen
    def _get_image_sample_label(self, index):
        # Obtener y regresar la etiqueta correspondiente en funcion del archivo csv que contiene la metadata e informacion necesaria
        if self.individual:
            return self.annotations.iloc[index, 2] # labels = [0 = 0, 1=1, ..., 10 = a, ..., 61 = Z]
        else:
            return self.annotations.iloc[index, 4]

# Prueba para identificar que las funciones descritas funcionen correctamente
if __name__ == "__main__":
    ANNOTATIONS_FILE = "Caracteres_Metadata.csv"
    IMAGE_DIR = "CARACTERES"

    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    print(f"Using device {device}")

    usd = CaracterDataset(ANNOTATIONS_FILE, IMAGE_DIR, device)
    print(f"There are {len(usd)} samples in the dataset.")
    img, label = usd[10000]