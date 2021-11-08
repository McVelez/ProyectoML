import os
import torch
from torch.utils.data import Dataset
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import cv2

class CaracterDataset(Dataset):

    def __init__(self, annotations_file, image_dir, device):
        self.annotations = pd.read_csv(annotations_file)
        self.image_dir = image_dir
        self.device = device

    # Para identificar la cantidad de archivos en el dataset
    def __len__(self):
        return len(self.annotations)

    # GetItem para acceder items del dataset
    def __getitem__(self, index):
        image_sample_path = self._get_image_sample_path(index)
        label = self._get_image_sample_label(index)
        img = cv2.imread(image_sample_path)
        #print(f"Training {image_sample_path}")
        img = torch.from_numpy(img)
        img = torch.Tensor.float(img)
        img = img.to(self.device)
        img = self._mix_down_if_necessary(img) # Reducir a un solo canal 
        return img, label

    def _mix_down_if_necessary(self, img):
        if img.shape[0] > 1: 
            img = torch.mean(img, dim=0, keepdim=True)
        return img

    def _get_image_sample_path(self, index):
        fold = f"fold{self.annotations.iloc[index, 2]}" # index para fila y columna 3 ya que es la columna de fold en el archivo csv
        filename = self.annotations.iloc[index, 3]
        path = os.path.join(self.image_dir, fold, filename)
        return path

    def _get_image_sample_label(self, index):
        return self.annotations.iloc[index, 2] # labels = [0 = 0, 1=1, ..., 10 = a, ..., 61 = Z]

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
    #img.show()