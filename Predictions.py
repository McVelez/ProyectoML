import torch
from CustomDataset import CaracterDataset
from ModeloCNN import CNNNetwork

# Lista de los caracteres posibles para su futuro mapeo

class_mapping = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
]

def predict(model, input, target, class_mapping):
    # Establecemos el modelo en modo de evaluación
    model.eval()
    # Uso de modulo para hacer predicciones de manera eficiente
    with torch.no_grad():
        # Inicializamos el modelo con parametro input
        predictions = model(input)
        # Creamos objeto tensor (1, 10) -> [ [0.1, 0.01, ..., 0.6] ]
        predicted_index = predictions[0].argmax(0)
        # Mapeamos el indice que el modelo predijo al caracter correspondiente
        predicted = class_mapping[predicted_index]
        # Mapeamos el indice que el caracter correcto al caracter correspondiente
        expected = class_mapping[target]

    return predicted, expected

if __name__ == "__main__":

    
    # Cargar el modelo entrenado
    cnn = CNNNetwork(1024)
    # Se carga diccionario de python que mapea cada capa a su parametro tensor
    state_dict = torch.load("cnn_caracteres.pth", map_location=torch.device('cpu'))
    # Cargamos el state_dict con
    cnn.load_state_dict(state_dict)
    
    # Cargar el dataset
    ANNOTATIONS_FILE = 'Caracteres_Metadata.csv'
    # Establecemos el nombre del directorio donde están las imágenes
    IMG_DIR = "CARACTERES"
    # Inicializamos CaracterDataset con el csv de annotations, directorio y cpu
    mds = CaracterDataset(ANNOTATIONS_FILE, IMG_DIR, "cpu")
    print("Espere un momento, esto puede tomar 1-2 minutos... se estan validando {0} archivos de imagen".format(len(mds)))

    # Contador de predicciones acertadas por el modelo
    rightPredictions = 0

    # Por cada objeto en el caracterDataset
    for i in range(len(mds)):
        input, target = mds[i][0], mds[i][1]
        input.unsqueeze_(0)

        # Relizar prediccion
        predicted, expected = predict(cnn, input, target, class_mapping)
        
        # Si la predicción del modelo acierta el caracter
        if(predicted == expected):
            print(f"Predicted: '{predicted}', expected: '{expected}'")
            # Se incrementa el contador de predicciones correctas
            rightPredictions += 1
            
    print("La cantidad de predicciones totales correctas fueron {0} de {1}".format(rightPredictions, len(mds)))
    # En base a las predicciones correctas obtenemos el porcentaje de eficiencia
    porcentaje = (rightPredictions * 100) / len(mds) 
    print(f"Porcentaje de eficiencia: {porcentaje}%")

   
