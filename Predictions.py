import torch
from CustomDataset import MedleyDataset
from ModeloCNN import CNNNetwork
from Training import SAMPLE_RATE, NUM_SAMPLES
import torchaudio

class_mapping = [
    "guitar",
    "flute",
    "piano",
    "violin"
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

    modeloPorUtilizar = input("TIPO DE MODELO QUE QUIERE UTILIZAR (default = [3] mfcc): [1] spectrogram | [2] melspectrogram | [3] mfcc \n")
    if modeloPorUtilizar == 1:
        cnn = CNNNetwork(2560)
        state_dict = torch.load("cnn_1.pth")
        transformada =  torchaudio.transforms.MelSpectrogram(sample_rate=SAMPLE_RATE, n_fft=1024, hop_length=512, n_mels=64)
    elif modeloPorUtilizar == 2:
        cnn = CNNNetwork(16896)
        state_dict = torch.load("cnn_2.pth")
        transformada = torchaudio.transforms.Spectrogram(n_fft=1024, hop_length=512)
    else:
        cnn = CNNNetwork(4096)
        state_dict = torch.load("cnn_3.pth")
        transformada = torchaudio.transforms.MFCC(sample_rate=SAMPLE_RATE)
    cnn.load_state_dict(state_dict)
    
    # Cargar el dataset
    datasetPorUtilizar = input("DATASET POR UTILIZAR (default = [1] medleys): [1] medleys | [2] irmas \n")
    if datasetPorUtilizar == 2:
        ANNOTATIONS_FILE = "IRMAS_Metadata.csv"
        AUDIO_DIR = "IRMAS_Subset"
        datasetEvaluado = "IRMAS"
        numberOfData = 2512
    else:
        ANNOTATIONS_FILE = 'Medley-solos-DB_metadata.csv'
        AUDIO_DIR = "audio"
        datasetEvaluado = "MedleyS"
        numberOfData = 14630
    mds = MedleyDataset(ANNOTATIONS_FILE, AUDIO_DIR, transformada, SAMPLE_RATE, NUM_SAMPLES, "cpu", datasetEvaluado)

    # Obtener muestra del dataset de MedleyS
    sum = 0

    guitarGuitar = 0
    guitarFlute = 0
    guitarPiano = 0
    guitarViolin = 0

    fluteGuitar = 0
    fluteFlute = 0
    flutePiano = 0
    fluteViolin = 0

    pianoGuitar = 0
    pianoFlute = 0
    pianoPiano = 0
    pianoViolin = 0

    violinGuitar = 0
    violinFlute = 0
    violinPiano = 0
    violinViolin = 0

    print("Espere un momento, esto puede tomar 1-2 minutos...")

    for i in range(numberOfData):
        input, target = mds[i][0], mds[i][1]
        input.unsqueeze_(0)

        # Relizar prediccion
        predicted, expected = predict(cnn, input, target, class_mapping)
        print(f"Predicted: '{predicted}', expected: '{expected}'")

        if(predicted == expected):
            sum += 1
            
            if expected == "guitar":
                guitarGuitar += 1

            if expected == "flute":
                fluteFlute += 1

            if expected == "piano":
                pianoPiano += 1

            if expected == "violin":
                violinViolin += 1
        else:

            if predicted == "guitar":
                if expected == "flute":
                    guitarFlute +=1
                if expected == "piano":
                    guitarPiano +=1
                if expected == "violin":
                    guitarViolin +=1

            if predicted == "flute":
                if expected == "guitar":
                    fluteGuitar +=1
                if expected == "piano":
                    flutePiano +=1
                if expected == "violin":
                    fluteViolin +=1

            if predicted == "piano":
                if expected == "guitar":
                    pianoGuitar +=1
                if expected == "flute":
                    pianoFlute +=1
                if expected == "violin":
                    pianoViolin +=1
            
            if predicted == "violin":
                if expected == "guitar":
                    violinGuitar +=1
                if expected == "flute":
                    violinFlute +=1
                if expected == "piano":
                    violinPiano +=1
    
    print(f"La cantidad de predicciones totales correctas fueron {sum} de {numberOfData}")
    porcentaje = (sum * 100) / numberOfData 
    print(f"Porcentaje de eficiencia: {porcentaje}%")

    print("CONFUSSION MATRIX")
    listM = [
        ["", "G", "F", "P", "V"], 
        ["G", guitarGuitar, fluteGuitar, pianoGuitar, violinGuitar],
        ["F", guitarFlute, fluteFlute, pianoFlute, violinFlute],
        ["P", guitarPiano, flutePiano, pianoPiano, violinPiano],
        ["V", guitarViolin, fluteViolin, pianoViolin, violinViolin]
    ]

    for tuple in listM:
        print(tuple)