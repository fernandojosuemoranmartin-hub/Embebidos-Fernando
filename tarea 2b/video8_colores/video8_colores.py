import cv2
import numpy as np

camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("Error: No se pudo abrir la camara")
    exit()

print("Deteccion de colores")
print("Presiona q para salir")

while True:

    ret, frame = camara.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # AZUL
    azul_bajo = np.array([100, 100, 20])
    azul_alto = np.array([130, 255, 255])

    mascara_azul = cv2.inRange(
        hsv,
        azul_bajo,
        azul_alto
    )

    # VERDE
    verde_bajo = np.array([35, 100, 20])
    verde_alto = np.array([85, 255, 255])

    mascara_verde = cv2.inRange(
        hsv,
        verde_bajo,
        verde_alto
    )

    cv2.imshow("Camara", frame)
    cv2.imshow("Color azul", mascara_azul)
    cv2.imshow("Color verde", mascara_verde)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
