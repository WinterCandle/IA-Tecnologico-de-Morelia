import cv2 as cv
import os
import numpy as np


data_path = 'rostros'
personas = os.listdir(data_path)
print('Personas encontradas: ', personas)

labels = []
facesData = []
label = 0


for nombre_persona in personas:
    persona_path = data_path + '/' + nombre_persona
    print('Leyendo las imágenes de:', nombre_persona)
    
    for file_name in os.listdir(persona_path):
       
        imagen_path = persona_path + '/' + file_name
        imagen = cv.imread(imagen_path, 0)
        
 
        facesData.append(imagen)
        labels.append(label)
        
    label = label + 1


face_recognizer = cv.face.LBPHFaceRecognizer_create()

print("Entrenando el modelo... (Esto puede tardar unos momentos)")


face_recognizer.train(facesData, np.array(labels))


face_recognizer.write('modeloLBPHFace.xml')

print("¡Modelo entrenado y guardado con éxito como 'modeloLBPHFace.xml'!")