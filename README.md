# ProyectoML

**LIBRERÍAS REQUERIDAS**: OpenCV

  Para instalar OpenCV a traves de la terminal: py -m pip install opencv-python

**PREPROCESAMIENTO Y SEGMENTACIÓN**

Se necesitan dos carpetas con los siguientes nombres para poder realizar el preprocesamiento y segmentación con la funcionalidad del código proporcionado en el archivo de _ProcessAndSegmentation_:
  - _CaptchaDataset_          (Dataset de captchas alfanuméricos sin preprocesar o segmentar)
  - _CAPTCHAS_SEGMENTADOS_    (Folder que almacena todos los captchas preprocesados, segmentados y etiquetados)
    
**ENTRENAMIENTO**

Se necesita la carpeta con el siguiente nombre para poder realizar un entrenamiento propio del modelo (considere modificar la cantidad de EPOCHS en caso de ser necesario en el archivo de Training) el cual será utilizado junto con el archivo de _Caracteres_Metadata.csv_ para realizar el entrenamiento del modelo CNN desde el archivo _Training_:
    - _CARACTERES_ (55,800 imágenes de entrenamiento. Link de drive: https://drive.google.com/file/d/1VM9YkSie2regeNvWN3LIAfvFt1LUA8O9/view?usp=sharing)

**PREDICCIONES**

Se necesita la carpeta con el siguiente nombre para poder calcular adecuadamente la eficiencia del modelo el cual será utilizado junto con el archivo de _Caracteres_validacion_Metadata.csv_ para realizar las predicciones en base al modelo entrenado en función del archivo py _Predictions_.
    - _CARACTERES_VALIDACION_ (8000 imágenes de validación. Link de drive: https://drive.google.com/file/d/1XNAWjAN9IzZsYl-RaM9YrqqCTiTC7cnj/view?usp=sharing)
    
  
