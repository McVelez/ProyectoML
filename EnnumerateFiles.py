import os 

for i in range(62):

    os.chdir(f'C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold{i}')

    incremental = 0
    for f in os.listdir():
        file_name, file_ext = os.path.splitext(f)
        number, caracter = file_name.split('_')
        newname = "{}_{}{}".format(incremental, caracter, file_ext)
        os.rename(f, newname)
        incremental += 1