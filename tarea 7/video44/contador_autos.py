import cv2
import os

# Carpeta donde está el código
carpeta = os.path.dirname(os.path.abspath(__file__))

# Ruta del video
ruta_video = os.path.join(carpeta, "autos.mp4")

# Abrir video
cap = cv2.VideoCapture(ruta_video)

if not cap.isOpened():
    print("No se pudo abrir el video")
    exit()

# Sustractor de fondo
fondo = cv2.createBackgroundSubtractorMOG2(
    history=100,
    varThreshold=35,
    detectShadows=False
)

contador = 0

# Línea vertical de conteo
linea_x = 400

# Para evitar contar varias veces
centros_contados = []

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (800, 500))

    # Aplicar sustracción de fondo
    mascara = fondo.apply(frame)

    # Limpiar ruido
    mascara = cv2.GaussianBlur(mascara, (5, 5), 0)

    _, mascara = cv2.threshold(
        mascara,
        180,
        255,
        cv2.THRESH_BINARY
    )

    mascara = cv2.dilate(
        mascara,
        None,
        iterations=2
    )

    # Buscar contornos
    contornos, _ = cv2.findContours(
        mascara,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Dibujar línea vertical
    cv2.line(
        frame,
        (linea_x, 0),
        (linea_x, 500),
        (0, 0, 255),
        3
    )

    for contorno in contornos:

        area = cv2.contourArea(contorno)

        if area < 1200:
            continue

        x, y, w, h = cv2.boundingRect(contorno)

        cx = x + w // 2
        cy = y + h // 2

        # Rectángulo verde
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Centro azul
        cv2.circle(
            frame,
            (cx, cy),
            5,
            (255, 0, 0),
            -1
        )

        # Si el centro cruza la línea
        if linea_x - 10 < cx < linea_x + 10:

            nuevo = True

            for punto in centros_contados:

                px, py = punto

                distancia = ((cx - px)**2 + (cy - py)**2)**0.5

                if distancia < 80:
                    nuevo = False
                    break

            if nuevo:
                contador += 1
                centros_contados.append((cx, cy))

    # Mostrar contador
    cv2.putText(
        frame,
        f"Autos: {contador}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    cv2.imshow("Contador de autos", frame)
    cv2.imshow("Mascara", mascara)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Total de autos:", contador)
