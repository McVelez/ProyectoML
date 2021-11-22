from CustomDataset import CaracterDataset
from ModeloCNN import CNNNetwork
import torch
from torch import nn
from torch.utils.data import DataLoader

# Variables requeridas para el acceso de los archivos por entrenar
ANNOTATIONS_FILE = 'Caracteres_Metadata.csv'
IMAGE_DIR = 'CARACTERES'

# Variables requeridas para el entrenamiento del modelo
BATCH_SIZE = 128
EPOCHS = 500
LEARNING_RATE = .001

# Funcion para crear un data loader, el cual permite realizar el entrenamiento en grupos 
def create_data_loader(train_data, batch_size):
    train_dataLoader = DataLoader(train_data, batch_size=batch_size)
    return train_dataLoader

# Funcion para realizar el entrenamiento de cada epoch individual
def train_one_epoch(model, data_loader, loss_fn, optimiser, device):
    # Por cada iteracion del grupo considerado en el data_loader se obtienen el valor de input (Imagen) y el target (Etiqueta)
    for input, target in data_loader: 
        # Se asignan las dos variables al dispositivo disponible
        input, target = input.to(device), target.to(device)

        # Se realiza la prediccion en base a las consideraciones y patrones que identifica el modelo
        prediction = model(input)

        # En base a la prediccion y a la etiqueta real de la imagen se calcula un valor de perdida
        loss = loss_fn(prediction, target)

        # En base al valor de perdida se realiza una optimizacion y modificacion de los parametros del modelo (filtros)
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()

    # Se imprime la perdida de cada epocha (el valor se encuentra normalizado para que siempre sea entre 0 y 1)
    print(f"Loss: {loss.item()}")

# Funcion de entrenamiento general de todo el modelo
def train(model, data_loader, loss_fn, optimiser, device, epochs):
    # Iteracion sobre la cantidad de epochs especificado (En nuestro caso utilizamos 500)
    for i in range(epochs):
        print(f"Epoch {i+1}")
        train_one_epoch(model, data_loader, loss_fn, optimiser, device)
        print("-----------------")
    print("Training complete")

# Entrenamiento del modelo
if __name__ == "__main__":
    # Seleccionar GPU o CPU para entrenamiento
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"
    print(f"Using {device}")
    
    # Cargar el dataset utilizado
    modelo = CaracterDataset(ANNOTATIONS_FILE, IMAGE_DIR, device)

    # Crear el data loader 
    train_dataloader = create_data_loader(modelo, BATCH_SIZE)

    # Construir el modelo CNN y asignar a GPU o CPU identificado
    cnn = CNNNetwork(1024).to(device)

    # Inicializar funcón de perdida y optimizacion
    loss_fn = nn.CrossEntropyLoss()
    optimiser = torch.optim.Adam(cnn.parameters(), lr=LEARNING_RATE)

    # Entrenar modelo
    train(cnn, train_dataloader, loss_fn, optimiser, device, EPOCHS)

    # Guardar modelo
    torch.save(cnn.state_dict(), "cnn_caracteres.pth")
    print("Model trained and stored at cnn_caracteres.pth")
  