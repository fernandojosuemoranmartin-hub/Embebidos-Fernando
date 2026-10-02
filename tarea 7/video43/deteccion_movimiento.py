import cv2

# Abrir cámara
cap = cv2.VideoCapture(0)

# Leer primer cuadro
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():

    # Diferencia entre cuadros
    diferencia = cv2.absdiff(frame1, frame2)

    # Convertir a escala de grises
    gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)

    # Suavizar
    blur = cv2.GaussianBlur(gris, (5, 5), 0)

    # Crear imagen binaria
    _, thresh = cv2.threshold(
        blur,
        20,
        255,
        cv2.THRESH_BINARY
    )

    # Expandir zonas detectadas
    dilatada = cv2.dilate(thresh, None, iterations=3)

    # Buscar contornos
    contornos, _ = cv2.findContours(
        dilatada,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contorno in contornos:

        # Ignorar movimientos muy pequeños
        if cv2.contourArea(contorno) < 1500:
            continue

        x, y, w, h = cv2.boundingRect(contorno)

        # Dibujar rectángulo
        cv2.rectangle(
            frame1,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Texto
        cv2.putText(
            frame1,
            "Movimiento detectado",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Mostrar resultado
    cv2.imshow("Deteccion de movimiento", frame1)

    # Actualizar cuadros
    frame1 = frame2

    ret, frame2 = cap.read()

    if not ret:
        break

    # Salir con Q
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
