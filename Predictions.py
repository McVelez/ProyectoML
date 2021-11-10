import torch
from CustomDataset import CaracterDataset
from ModeloCNN import CNNNetwork

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
    model.eval()
    with torch.no_grad():
        predictions = model(input)
        # Tensor object (1, 10) -> [ [0.1, 0.01, ..., 0.6] ]
        predicted_index = predictions[0].argmax(0)
        predicted = class_mapping[predicted_index]
        expected = class_mapping[target]
    return predicted, expected

if __name__ == "__main__":

    
    # Cargar el modelo entrenado
    cnn = CNNNetwork(1024)
    state_dict = torch.load("cnn_caracteres.pth", map_location=torch.device('cpu'))
    cnn.load_state_dict(state_dict)
    
    # Cargar el dataset
    ANNOTATIONS_FILE = 'Caracteres_Metadata.csv'
    IMG_DIR = "CARACTERES"
    mds = CaracterDataset(ANNOTATIONS_FILE, IMG_DIR, "cpu")   
    print("Espere un momento, esto puede tomar 1-2 minutos... se estan validando {0} archivos de imagen".format(len(mds)))

    rightPredictions = 0
    for i in range(len(mds)):
        input, target = mds[i][0], mds[i][1]
        input.unsqueeze_(0)

        # Relizar prediccion
        predicted, expected = predict(cnn, input, target, class_mapping)
        
        if(predicted == expected):
            print(f"Predicted: '{predicted}', expected: '{expected}'")
            rightPredictions += 1
            
    print("La cantidad de predicciones totales correctas fueron {0} de {1}".format(rightPredictions, len(mds)))
    porcentaje = (rightPredictions * 100) / len(mds) 
    print(f"Porcentaje de eficiencia: {porcentaje}%")

   