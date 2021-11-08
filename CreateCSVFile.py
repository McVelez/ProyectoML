import os 
import pandas as pd

everything = []

for i in range(62):

    os.chdir(f'C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold{i}')

    # subset  , caracter, fold, nameOfFile
    # training, 0       , 0   , 0_0.PNG

    for f in os.listdir():
        file_name, file_ext = os.path.splitext(f)
        number, caracter = file_name.split('_')
        

        row = ["training", caracter, i, f]

        everything.append(row)


df = pd.DataFrame(everything)

df.to_csv('Caracteres_Metadata.csv')