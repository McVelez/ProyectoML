import os 
import shutil

# Medley-solos-DB_test-1_0b675ade-f1a7-5bf2-f089-af154ba9bf36.wav

os.chdir('C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CAPTCHAS_SEGMENTADOS')

cant = 0
limit = 55800

rootdir = 'C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CAPTCHAS_SEGMENTADOS'

folderDir = 'C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES'

'''
os.chdir(folderDir)
for i in range(62):
    os.mkdir(f"fold{i}")
'''


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        _ , lodemas = file.split('_')
        caracter, extension = lodemas.split('.')

        print(subdir)

        sourcepath = f"{subdir}/{file}"

        if(cant <= limit):
            if caracter == "0":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold0/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "1":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold1/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "2":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold2/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "3":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold3/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "4":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold4/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "5":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold5/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "6":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold6/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "7":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold7/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "8":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold8/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "9":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold9/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "a":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold10/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "b":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold11/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "c":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold12/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "d":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold13/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "e":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold14/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "f":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold15/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "g":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold16/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "h":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold17/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "i":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold18/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "j":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold19/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "k":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold20/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "l":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold21/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "m":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold22/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "n":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold23/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "o":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold24/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "p":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold25/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "q":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold26/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "r":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold27/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "s":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold28/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "t":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold29/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "u":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold30/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "v":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold31/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "w":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold32/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "x":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold33/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "y":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold34/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "z":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold35/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "A":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold36/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "B":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold37/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "C":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold38/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "D":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold39/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "E":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold40/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "F":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold41/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "G":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold42/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "H":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold43/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "I":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold44/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "J":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold45/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "K":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold46/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "L":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold47/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "M":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold48/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "N":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold49/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "O":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold50/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "P":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold51/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "Q":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold52/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "R":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold53/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "S":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold54/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "T":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold55/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "U":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold56/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "V":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold57/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "W":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold58/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "X":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold59/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "Y":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold60/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
            if caracter == "Z":
                dst_path = f"C:/Users/marco/OneDrive/Desktop/ML_ImagePreprocessing/CARACTERES/fold61/{cant}_{caracter}.PNG"
                shutil.move(sourcepath, dst_path)
           
            cant += 1


        
        
        
        

        
            
        

        #print(file)



