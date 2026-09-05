import cv2
import numpy as np

# Abrir la camara
camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("Error: No se pudo abrir la camara")
    exit()

print("Deteccion de colores")
print("Azul y Verde")
print("Presiona q para salir")

while True:

    ret, frame = camara.read()

    if not ret:
        print("Error al capturar imagen")
        break

    # Convertir la imagen de BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ==========================================
    # COLOR AZUL
    # ==========================================

    azul_bajo = np.array([100, 100, 20])
    azul_alto = np.array([130, 255, 255])

    mascara_azul = cv2.inRange(
        hsv,
        azul_bajo,
        azul_alto
    )

    # Buscar contornos azules
    contornos_azul, _ = cv2.findContours(
        mascara_azul,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contorno in contornos_azul:

        area = cv2.contourArea(contorno)

        # Ignorar objetos muy pequeños
        if area > 500:

            # Dibujar contorno
            cv2.drawContours(
                frame,
                [contorno],
                -1,
                (255, 0, 0),
                3
            )

            # Obtener posicion del objeto
            x, y, w, h = cv2.boundingRect(contorno)

            # Calcular centro
            cx = x + w // 2
            cy = y + h // 2

            # Dibujar punto en el centro
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (255, 255, 255),
                -1
            )

            # Escribir nombre del color
            cv2.putText(
                frame,
                "AZUL",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 0, 0),
                2
            )

            # Mostrar coordenadas
            cv2.putText(
                frame,
                f"X:{cx} Y:{cy}",
                (x, y + h + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

    # ==========================================
    # COLOR VERDE
    # ==========================================

    verde_bajo = np.array([35, 100, 20])
    verde_alto = np.array([85, 255, 255])

    mascara_verde = cv2.inRange(
        hsv,
        verde_bajo,
        verde_alto
    )

    # Buscar contornos verdes
    contornos_verde, _ = cv2.findContours(
        mascara_verde,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contorno in contornos_verde:

        area = cv2.contourArea(contorno)

        if area > 500:

            # Dibujar contorno
            cv2.drawContours(
                frame,
                [contorno],
                -1,
                (0, 255, 0),
                3
            )

            # Obtener posicion
            x, y, w, h = cv2.boundingRect(contorno)

            # Calcular centro
            cx = x + w // 2
            cy = y + h // 2

            # Dibujar punto central
            cv2.circle(
                frame,
                (cx, cy),
                5,
                (255, 255, 255),
                -1
            )

            # Nombre del color
            cv2.putText(
                frame,
                "VERDE",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # Coordenadas
            cv2.putText(
                frame,
                f"X:{cx} Y:{cy}",
                (x, y + h + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )

    # ==========================================
    # MOSTRAR RESULTADOS
    # ==========================================

    cv2.imshow("Deteccion de colores", frame)
    cv2.imshow("Mascara Azul", mascara_azul)
    cv2.imshow("Mascara Verde", mascara_verde)

    # Presionar q para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camara.release()
cv2.destroyAllWindows()

print("Programa terminado")
