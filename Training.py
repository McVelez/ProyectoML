from CustomDataset import CaracterDataset
from ModeloCNN import CNNNetwork
import torch
from torch import nn
from torch.utils.data import DataLoader

ANNOTATIONS_FILE = 'Caracteres_Metadata.csv'
IMAGE_DIR = 'CARACTERES'

BATCH_SIZE = 128
EPOCHS = 10
LEARNING_RATE = .001

def create_data_loader(train_data, batch_size):
    train_dataLoader = DataLoader(train_data, batch_size=batch_size)
    return train_dataLoader

def train_one_epoch(model, data_loader, loss_fn, optimiser, device):
    for input, target in data_loader:
        
        input, target = input.to(device), target.to(device)

        # calculate loss 
        prediction = model(input)
        loss = loss_fn(prediction, target)
        # backpropagate loss and update weights
        optimiser.zero_grad()
        loss.backward()
        optimiser.step()

    print(f"Loss: {loss.item()}")

def train(model, data_loader, loss_fn, optimiser, device, epochs):
    for i in range(epochs):
        print(f"Epoch {i+1}")
        train_one_epoch(model, data_loader, loss_fn, optimiser, device)
        print("-----------------")
    print("Training complete")

if __name__ == "__main__":
    # Seleccionar GPU o CPU para entrenamiento
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"

    print(f"Using {device}")
    
    modelo = CaracterDataset(ANNOTATIONS_FILE, IMAGE_DIR, device)

    train_dataloader = create_data_loader(modelo, BATCH_SIZE)

    # Build model y asignar a GPU o CPU identificado
    cnn = CNNNetwork(1024).to(device)
    # Inicializar funcón de loss y optimiser
    loss_fn = nn.CrossEntropyLoss()
    optimiser = torch.optim.Adam(cnn.parameters(), lr=LEARNING_RATE)
    # Entrenar modelo
    train(cnn, train_dataloader, loss_fn, optimiser, device, EPOCHS)

    # Guardar modelo
    torch.save(cnn.state_dict(), "cnn_caracteres.pth")
    print("Model trained and stored at cnn_caracteres.pth")
  