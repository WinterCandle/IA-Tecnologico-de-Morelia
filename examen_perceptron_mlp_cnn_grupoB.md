           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            EXAMEN TEÓRICO — PERCEPTRÓN, MLP Y CNN (GRUPO B)

                            Eduardo Alcaraz
           ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


1 Datos del alumno
══════════════════

  ━━━━━━━━━━━
   Nombre Miguel Angel Murillo Renteria  
   Grupo   B 
   Fecha  13/03/2026 
  ━━━━━━━━━━━


2 Pregunta 1 — Por qué no basta “una sola neurona”
══════════════════════════════════════════════════

  1. Resume el funcionamiento de un perceptrón como “regla de decisión”.
  2. Explica la noción de *frontera lineal* sin escribir fórmulas.
  3. Da un ejemplo (aunque sea inventado) donde esa frontera *no*
     alcanza.


2.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.-Básicamente, funciona como un juez. Recibe varios datos, le da un "peso" o importancia a cada uno y los suma. Si el total pasa de cierto límite, dice que sí; si no, dice que no.

2.-Imagina que tienes tus datos dibujados como puntos en un papel. La frontera lineal es tratar de separar los de una clase y otra trazando una sola línea recta con una regla.

3.-Piensa en un tablero de ajedrez. Si intentas separar las casillas blancas de las negras usando una sola línea recta, rápido te das cuenta de que es imposible.

  └────


3 Pregunta 2 — CNN: de píxeles a mapas
══════════════════════════════════════

  1. ¿Qué problema de *estructura espacial* ignora un MLP si aplana la
     foto?
  2. ¿Qué significa que un mismo filtro se aplique en toda la imagen?
  3. Además de clasificación de objetos, cita *dos* usos donde la CNN
     encaja bien.


3.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- Si agarramos una foto y la aplanamos para meterla a un MLP, le rompemos toda la estructura espacial. Perdemos el contexto de qué píxel está arriba o al lado de cuál, y adiós a las formas y texturas.

2.- Es como agarrar una lupa con un patrón específico (por ejemplo, que busque bordes verticales) y deslizarla por toda la foto. Busca exactamente lo mismo sin importarle en qué parte de la imagen esté.

3.-Aparte de clasificar objetos, queda súper bien para diagnósticos médicos (como buscar tumores en radiografías) o en sistemas de seguridad biométrica (como el desbloqueo facial del celular).

  └────


4 Pregunta 3 — Softmax, clases y decisiones
═══════════════════════════════════════════

  1. Diferencia un problema *binario* de uno *multiclase* en términos de
     salida de la red.
  2. ¿Qué lectura le das a las probabilidades que produce un softmax?
  3. Imagina tres carpetas de imágenes (tres riesgos o tres animales):
     ¿qué arquitectura de *salida* usarías y por qué?


4.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.-En un problema binario, con una sola salida nos basta para saber qué tan probable es A contra B. En multiclase, ocupamos varias salidas, una dedicada a cada categoría posible.

2.-Softmax agarra los números crudos de la red y los transforma en porcentajes fáciles de leer que siempre suman 100%. Así, te arroja algo como: "Estoy 80% seguro de que es perro, 15% gato y 5% pájaro".

3.-Usaría una capa de salida con tres neuronas y activación Softmax. Así tendría tres porcentajes compitiendo, y la decisión final se la lleva la carpeta con el porcentaje más alto.

  └────


5 Pregunta 4 — MLP: profundidad con sentido
═══════════════════════════════════════════

  1. ¿Qué ganas al apilar capas densas con activaciones no lineales?
  2. ¿Qué riesgo aparece si la red es *demasiado* grande para tus datos?
  3. Relaciona “capa oculta” con la idea de aprender representaciones
     intermedias (en palabras simples).


5.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- Ganas la capacidad de aprender patrones complejos y curvas. Si solo apilas capas densas sin activar la no linealidad, es como sumar puras líneas rectas: el resultado va a ser otra línea recta y la red no aprende nada útil.

2.- Cae en sobreajuste (overfitting). La red es tan grande que literal se pone a "machetear" y se memoriza los datos de entrenamiento. Cuando le pasas datos nuevos, truena.

3.- Míralo como resolver un problema por pasos. La primera capa oculta detecta cosas súper simples como líneas, la siguiente junta esas líneas para armar figuras, y la última ya te reconoce el objeto completo.


6 Pregunta 5 — Entrenamiento sin magia
══════════════════════════════════════

  1. Explica qué es una *época* a nivel intuitivo.
  2. ¿Hacia qué “objetivo” se mueven los pesos cuando hablamos de
     minimizar el error?
  3. Si el learning rate es absurdo (muy grande o muy chico), ¿qué
     síntomas conceptuales esperarías?


6.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- A nivel intuitivo, una época es darle a la red una pasada completa por absolutamente todos tus datos. Es como leerte un libro de texto de principio a fin una vez.

2.- Se mueven para intentar reducir el error a cero. El chiste es que la predicción de la red termine siendo igualita a la respuesta real que ya conocemos.

3.- Si el learning rate es muy grande, la red da brincos enormes, se vuelve inestable y nunca le atina al punto de menor error. Si es muy chico, da pasos milimétricos y se queda estancada; va a tardar una eternidad en aprender.
  └────


7 Pregunta 6 — Bloques de una CNN
═════════════════════════════════

  Sin matemáticas, di el papel de cada pieza:
  1. Kernel / filtro convolucional
  2. Función de activación después de conv
  3. Max pooling
  4. Capa densa + softmax al final de un clasificador


7.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- Filtro: Es como una linterna que va escaneando la imagen buscando cosas muy puntuales, como bordes, esquinas o cambios bruscos de color.

2.- Activación (tipo ReLU): Sirve para decidir qué pasa y qué no. Si el filtro detectó algo útil, lo deja pasar; si no, lo apaga (lo manda a cero). Esto le da a la red flexibilidad para aprender formas complejas.

3.- Max pooling: Básicamente es un resumidor. Toma pedacitos de la imagen, se queda solo con lo que resalta más y reduce el tamaño de todo para no saturar a la red con información inútil.

4.- Densa + Softmax: Recibe todo el resumen de características que armaron los filtros y toma la decisión final, calculando las probabilidades para cada clase.
  └────


8 Pregunta 7 — XOR y la historia del aprendizaje
════════════════════════════════════════════════

  1. ¿Por qué XOR se volvió un “contraejemplo” famoso?
  2. ¿Qué elemento de un MLP permite patrones que no son una sola línea?
  3. ¿En qué tipo de tabla/problema del mundo real seguirías usando algo
     tan simple como un perceptrón o un modelo lineal?


8.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- Fue famoso porque demostró matemáticamente que un perceptrón simple no podía resolver ni un problema de lógica súper básico (XOR). Eso decepcionó a la comunidad y estancó la IA un buen rato.

2.- Lo que rompe esa limitación es meterle capas ocultas combinadas con funciones de activación no lineales.

3.- Yo lo usaría para predecir el precio de una casa basado en los metros cuadrados, por ejemplo. Como es una relación muy directa y proporcional, un modelo lineal simple hace la chamba sin problema.

  └────


9 Pregunta 8 — De lo simple a lo abstracto en visión
════════════════════════════════════════════════════

  1. Contrasta lo que buscan capas tempranas vs capas profundas en una
     CNN.
  2. ¿Qué intuición da eso para *transfer learning* (aunque no lo hayas
     programado)?
  3. ¿Cuándo sospecharías que tu CNN es “profunda de más” para el
     dataset del curso?


9.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- Las primeras capas buscan cosas muy elementales, como rayitas, sombreados o plastas de color. Las más profundas van combinando todo eso para detectar conceptos ya armados, como ojos, llantas de un carro o el hocico de un perro.

2.- La intuición del transfer learning es que, como las primeras capas siempre aprenden a detectar líneas y bordes básicos, puedes reciclar esa parte de una red que alguien más ya entrenó y solo ponerte a enseñarle a las últimas capas a reconocer tus objetos en particular. Te ahorra muchísimo tiempo de cómputo.

3.- Sospecharía de eso cuando el modelo saca un 100% perfecto en el entrenamiento, pero lo pones a prueba con imágenes que no conoce y reprueba miserablemente. Eso grita que solo se memorizó el dataset.
  └────


10 Pregunta 9 — Análisis: matching problema → modelo
════════════════════════════════════════════════════

  Elige *Perceptrón/lineal* / *MLP* / *CNN* (una opción) y justifica en
  una frase:

  1. Predecir “compra / no compra” con edad, ingreso y visitas a la web
     (columnas numéricas).
  2. Detectar si hay un gato en una foto.
  3. Aproximar una frontera “curva” o a trozos en datos 2D tabulares.
  4. ¿CNN es la herramienta natural para predecir la siguiente palabra
     de un párrafo? Justifica y nombra una familia del curso más
     adecuada (RNN/Transformer a nivel nombre).


10.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- MLP. Es el modelo ideal para cruzar columnas numéricas en tablas y encontrar patrones complejos que no son imágenes.

2.- CNN. Es la arquitectura hecha a la medida para procesar píxeles respetando su orden espacial y buscar patrones visuales.

3.- Al tener capas ocultas y activaciones no lineales, es capaz de doblar la frontera de decisión para adaptarse a curvas en datos tabulares.

4.- No. El texto depende totalmente de su orden y secuencia en el tiempo, y la CNN está pensada para espacio estático. La familia natural aquí sería una RNN (Redes Neuronales Recurrentes) o un Transformer.

  └────


11 Pregunta 10 — Análisis: auditoría de un equipo
═════════════════════════════════════════════════

  Un equipo entrega un modelo “muy preciso” en su laptop y falla con
  datos nuevos.

  1. ¿Qué diagnósticos conceptuales harías *antes* de tocar
     hiperparámetros al azar?
  2. Pide *dos* evidencias que deberían mostrar en la defensa (curvas,
     separación train/val, ejemplos de error, etc.).
  3. Redacta *tres* preguntas tuyas para comprobar si saben cuándo usar
     perceptrón, MLP o CNN (distintas a las del Grupo A si las conoces).


11.0.1 Respuesta
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌

  ┌────
1.- De entrada, es un caso de librito de overfitting (sobreajuste). El modelo simplemente se "macheteó" los datos locales por tener demasiada complejidad o porque hicieron mal la división entre entrenamiento y prueba. No le movería a los hiperparámetros sin revisar eso primero.

2.- Les pediría la gráfica de pérdida (loss) para ver en qué época la curva de validación se separó de la de entrenamiento y se disparó hacia arriba, y además, pruebas reales corriendo el modelo sobre un dataset de validación que la red no haya visto jamás.

3.-

    Si los datos fueran de un Excel con historiales clínicos numéricos, ¿por qué meterle una CNN sería una mala idea?

    ¿Qué técnica exacta implementaron para comprobar que el modelo está generalizando y no solo memorizó los datos de su laptop?

    Si mañana el cliente nos pide clasificar 5 cosas en vez de 2, ¿qué partes de la capa de salida tendrían que modificar?

  └────
