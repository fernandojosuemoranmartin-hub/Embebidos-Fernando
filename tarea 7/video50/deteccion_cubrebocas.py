import cv2

# Detectores incluidos en OpenCV
detector_rostro = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

detector_ojos = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Abrir cámara
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        print("No se pudo abrir la cámara")
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    rostros = detector_rostro.detectMultiScale(
        gris,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80, 80)
    )

    # Detectar ojos
    ojos = detector_ojos.detectMultiScale(
        gris,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(30, 30)
    )

    # Si detecta rostro completo
    if len(rostros) > 0:

        for (x, y, w, h) in rostros:

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 0, 255),
                2
            )

            cv2.putText(
                frame,
                "Sin cubrebocas",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

    # Si no detecta rostro pero sí ojos
    elif len(ojos) >= 2:

        cv2.putText(
            frame,
            "Posible cubrebocas",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        for (x, y, w, h) in ojos:

            cv2.rectangle(
                frame,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )

    else:

        cv2.putText(
            frame,
            "Rostro no detectado",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

    cv2.imshow("Deteccion de cubrebocas", frame)

    # Presiona Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
