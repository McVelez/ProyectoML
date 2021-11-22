# ProyectoML

**LIBRERÍAS REQUERIDAS**: OpenCV

  - Para instalar OpenCV a traves de la terminal: py -m pip install opencv-python

**PREPROCESAMIENTO Y SEGMENTACIÓN**

Se necesitan dos carpetas con los siguientes nombres para poder realizar el preprocesamiento y segmentación con la funcionalidad del código proporcionado en el archivo de _ProcessAndSegmentation.py_:
  - _CaptchaDataset_          (Dataset de captchas alfanuméricos sin preprocesar o segmentar)
  - _CAPTCHAS_SEGMENTADOS_    (Folder que almacena todos los captchas preprocesados, segmentados y etiquetados)
    
**ENTRENAMIENTO**

Se necesita la carpeta con el siguiente nombre para poder realizar un entrenamiento propio del modelo (considere modificar la cantidad de EPOCHS en caso de ser necesario en el archivo de Training) el cual será utilizado junto con el archivo de _Caracteres_Metadata.csv_ para realizar el entrenamiento del modelo CNN desde el archivo _Training.py_:
  - _CARACTERES_ (55,800 imágenes de entrenamiento. Link de drive: https://drive.google.com/file/d/1VM9YkSie2regeNvWN3LIAfvFt1LUA8O9/view?usp=sharing)

**PREDICCIONES**

Se necesita la carpeta con el siguiente nombre para poder calcular adecuadamente la eficiencia del modelo el cual será utilizado junto con el archivo de _Caracteres_validacion_Metadata.csv_ para realizar las predicciones en base al modelo entrenado en función del archivo _Predictions.py_.
  - _CARACTERES_VALIDACION_ (8000 imágenes de validación. Link de drive: https://drive.google.com/file/d/1XNAWjAN9IzZsYl-RaM9YrqqCTiTC7cnj/view?usp=sharing)

En caso de utilizar la validación de los captchas completos y no de los caracteres es necesario utilizar el archivo de _Captchas_validacion_Metadata.csv_ junto con la siguiente carpeta:
  - _CAPTCHAS_VALIDACION_ (800 folders de validación. Link de drive: https://drive.google.com/file/d/1mTHJm5cQeiXnF1JkJIofnjcYWk-cC_R9/view?usp=sharing)
    
  
