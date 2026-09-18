# Reporte EDA – Operación Dino Crash
**Analista:** Miguel Ángel Murillo Rentería

## 1. Problema y dataset (Misión 1)

### P1 – Muerte en el siguiente frame
- **Y:** `is_crash_next_frame` (Binaria: 1 = choca, 0 = sobrevive).
- **X (mínimo 5 variables):** `dist_obstacle` (px al obstáculo), `velocidad` (del juego), `tipo_obstaculo` (categórica), `posicion_y_dino` (altura actual), `is_ducking` (binaria, si está agachado).
- **Granularidad:** Un frame de una partida (cada ~16 ms).
- **Tamaño mínimo de dataset:** ~500,000 frames (se necesita muchísimo volumen porque los choques son raros comparados con los frames de supervivencia).

### P2 – Cuántos puntos alcanzará esta partida al morir
- **Y:** `puntuacion_final` (Numérica continua).
- **X (mínimo 5 variables):** `rango_jugador` (experiencia), `fps_promedio` (lag del PC), `intentos_sesion`, `high_score_jugador`, `hora_dia`.
- **Granularidad:** Una partida completa (desde Start hasta Game Over).
- **Tamaño mínimo de dataset:** ~10,000 partidas completas (para poder trazar una regresión que limpie el ruido del factor humano).

### P3 – Qué tipo de obstáculo viene próximo
- **Y:** `proximo_obstaculo` (Categórica multiclase).
- **X (mínimo 5 variables):** `score_actual`, `obstaculo_anterior`, `distancia_ultimo_spawn`, `velocidad`, `tipo_terreno_previo`.
- **Granularidad:** Por evento de generación (solo una fila en el instante que spawnea un objeto).
- **Tamaño mínimo de dataset:** ~5,000 eventos (para capturar la estadística del generador aleatorio RNG).

## 2. Diccionario y muestra (Misión 2)
- **Patrón en died=1:** El choque (frame 82) ocurre por una combinación de factores: el dino aterriza (`jump=0`) justo cuando la distancia al hitbox es casi nula (`dist_obstacle=12`). La intersección de estas variables espaciales en ese tick causa la muerte.
- **¿Falta alguna columna?:** Sí. `score` no predice un choque inmediato. Faltan variables físicas clave como `posicion_y` (para saber en qué fase del salto va) y `is_ducking`. Además, `died` describe el final, pero no sirve para entrenar P1; necesitamos desplazar esa columna (shift) para que el modelo aprenda *antes* de que pase.

## 3. Checklist EDA (Misión 3)
- **Balance de clase (P1):** Extremadamente desbalanceado. El 99.59% de los frames son ceros (sobrevivir). 
- **Leakage (fugas):** Si en P1 usáramos el `time_ms` final o el `score` total como variable de entrada, el modelo haría trampa leyendo el futuro. En entrenamiento sería perfecto, en vivo no sabría qué hacer.
- **i.i.d. (Independencia):** Mezclar frames sueltos en train/test es un error porque los frames son secuenciales (el frame 10 es casi igual al 9). Si no separamos por `session_id`, el modelo memoriza la partida en lugar de aprender a jugar.

## 4. Interpretación de resúmenes (Misión 4)
- **Desbalance y métricas:** Con solo 50 muertes en 12,000 frames, usar *Accuracy* es inútil (decir siempre "no salto" daría 99% de acierto pero perdería el juego). Se debe usar **F1-Score** para equilibrar Precision y Recall.
- **dist_obstacle:** Es un predictor excelente. El EDA muestra que los choques se agrupan cuando la distancia es < 20px, dándonos un umbral casi perfecto para separar clases.
- **Distribución de score:** Hay una asimetría brutal (media 28, máxima 120). Muchos mueren rápido y pocos duran mucho. Una regresión lineal simple fallaría aquí; se necesita transformar la variable o usar árboles.

## 5. Elección de modelo (Misiones 5-6)

| Escenario | Tras tu EDA, ¿qué aplica? | Modelo que propondrías |
| :--- | :--- | :--- |
| **P1** | Y binaria muy desbalanceada | Random Forest con pesos balanceados (class_weight) |
| **P2** | Y numérica (score final) | Árbol regresor |
| **P3** | Y categórica multiclase | Regresión Logística Multinomial / Árbol de decisión |

- **Contraejemplo (Red Neuronal Profunda):** Si intentáramos predecir el score (P2) usando un dataset tabular simple de 50 partidas, una Red Profunda haría *overfitting* masivo porque memorizaría los datos por falta de volumen.
- **Reglas fijas vs. Modelo (P1):** Usar reglas como `si dist < 15 y jump=0` funciona hasta que actualizan el juego. Si cambian la velocidad o el tamaño del cactus, la regla se rompe. Un modelo entrenado solo necesita tragar los nuevos datos para adaptarse solo.

## Síntesis
Primero pediría el dataset del Escenario P1, pero asegurando tener variables espaciales granulares y la variable objetivo desplazada al futuro (shift). El modelo definitivo lo elegiría *solo después* de que el EDA me confirme la magnitud del desbalanceo y las correlaciones; por ejemplo, al ver el sesgo extremo, descartaría modelos lineales simples y me iría directo por un ensamble de árboles que maneje bien las métricas asimétricas y umbrales duros.