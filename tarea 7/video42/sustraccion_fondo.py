import cv2

# Abrir cámara
cap = cv2.VideoCapture(0)

# Crear sustractor de fondo
fondo = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

while True:

    ret, frame = cap.read()

    if not ret:
        print("No se pudo abrir la cámara")
        break

    # Aplicar sustracción de fondo
    mascara = fondo.apply(frame)

    # Limpiar ruido
    mascara = cv2.medianBlur(mascara, 5)

    # Mostrar cámara normal
    cv2.imshow("Camara", frame)

    # Mostrar fondo sustraído
    cv2.imshow("Sustraccion de fondo", mascara)

    # Presiona Q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
