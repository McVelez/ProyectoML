#En este archivo se utiliza la librería de redes neuronales incluida en el modulo de PyTorch.
from torch import nn

#Se procede a instanciar una clase con el modulo importado para generar el modelo.
class CNNNetwork(nn.Module):

    def __init__(self, dimensiones):
        super().__init__()
        
        # Aqui se generan los 4 bloques cuya funcion principal es ser los filtros/capas del modelo y se ejecutara el proceso de la aplicación de filtros en el siguiente orden: 
        # Aplicación del filtro convolucional con la función "Conv2d" /  filtro de unidimensionamiento/flatten con la función de "ReLU" / y finalmente se realiza una transformación lineal con MaxPool2d 
        
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.conv3 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.conv4 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=2),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        #Flatten realiza la conversion de dimensiones a un solo plano.
        self.flatten = nn.Flatten()
        #Se ejecuta una transformación lineal en base a los resultados obtenidos. 
        self.linear = nn.Linear(dimensiones, 62)

    #La sección de "forward" acepta las entradas que se generaron en los bloques y posteriormente ejecuta los calculos y procedimientos de los filtros. 
    #Luego "encadena" las salidas a las entradas secuencialmente para cada módulo subsiguiente, finalmente devolviendo la salida del último módulo que se nombra "predictions".

    def forward(self, input_data):
        x = self.conv1(input_data)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.flatten(x)
        predictions = self.linear(x)
        return predictions

