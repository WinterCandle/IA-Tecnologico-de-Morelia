import cv2 as cv
import os


data_path = 'rostros'
personas = os.listdir(data_path)
print('Nombres reconocibles: ', personas)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('modeloLBPHFace.xml')


ruta_cascada = os.path.join(cv.data.haarcascades, 'haarcascade_frontalface_alt2.xml')
rostro_cascade = cv.CascadeClassifier(ruta_cascada)


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostros = rostro_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in rostros:
   
        rostro_recortado = gray[y:y+h, x:x+w]
        rostro_recortado = cv.resize(rostro_recortado, (100, 100))

      
        label, confianza = face_recognizer.predict(rostro_recortado)

      
        if confianza < 80:
            nombre = personas[label]
            color = (0, 255, 0)
            texto = f'{nombre} ({int(confianza)})'
        else:
            nombre = 'Desconocido'
            color = (0, 0, 255) 
            texto = f'Desconocido ({int(confianza)})'

      
        cv.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv.putText(frame, texto, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv.imshow('Reconocimiento Facial', frame)


    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
