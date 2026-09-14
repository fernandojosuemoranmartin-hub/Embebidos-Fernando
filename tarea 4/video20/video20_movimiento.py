import cv2

# Abrir la camara
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: No se pudo abrir la camara")
    exit()

i = 0

print("Deteccion de movimiento")
print("No muevas la camara al iniciar")
print("Presiona q para salir")

while True:

    ret, frame = video.read()

    if ret == False:
        break

    # Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Guardar el fondo despues de algunos frames
    if i == 20:
        fondo = gris.copy()
        print("Fondo capturado")

    # A partir del frame 21 comparar con el fondo
    if i > 20:

        # Diferencia entre el fondo y la imagen actual
        diferencia = cv2.absdiff(gris, fondo)

        # Convertir la diferencia a blanco y negro
        _, umbral = cv2.threshold(
            diferencia,
            40,
            255,
            cv2.THRESH_BINARY
        )

        # Encontrar contornos
        contornos, _ = cv2.findContours(
            umbral,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # Revisar cada contorno
        for contorno in contornos:

            area = cv2.contourArea(contorno)

            # Ignorar movimientos muy pequeños
            if area > 5000:

                x, y, w, h = cv2.boundingRect(contorno)

                # Dibujar rectangulo
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # Texto para indicar movimiento
                cv2.putText(
                    frame,
                    "MOVIMIENTO",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

        # Mostrar la imagen de diferencia
        cv2.imshow("Movimiento detectado", umbral)

    # Mostrar camara
    cv2.imshow("Camara", frame)

    i = i + 1

    # Presionar q para salir
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()

print("Programa terminado")
