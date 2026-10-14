import numpy as np
import cv2 as cv
import os


nombre_persona = 'Miguel'


carpeta_salida = f'rostros/{nombre_persona}'
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)


ruta_cascada = os.path.join(cv.data.haarcascades, 'haarcascade_frontalface_alt2.xml')
rostro = cv.CascadeClassifier(ruta_cascada)


cap = cv.VideoCapture(0) 

count = 0

while True:
    ret, frame = cap.read()
    if not ret: 
        print("No se pudo leer el video o la cámara.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in rostros:
   
        cv.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        
       
        img = frame[y:y+h, x:x+w]
        imgr = cv.resize(img, (100, 100))
        
        count = count + 1   
        
        
        name = f'{carpeta_salida}/rostro_{count}.jpg'
        cv.imwrite(name, imgr)
        
    cv.imshow('rostros', frame)
    
    k = cv.waitKey(1)
   
    if k == 27 or count >= 300:
        print(f"Finalizado. Se recolectaron {count} rostros de {nombre_persona}.")
        break

cap.release()
cv.destroyAllWindows()