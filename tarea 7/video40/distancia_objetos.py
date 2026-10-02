import cv2
import numpy as np
import os
import math
import glob

# Carpeta donde está este archivo
carpeta = os.path.dirname(os.path.abspath(__file__))

# Buscar automáticamente imágenes JPG, PNG o JPEG
imagenes = []

imagenes += glob.glob(os.path.join(carpeta, "*.jpg"))
imagenes += glob.glob(os.path.join(carpeta, "*.jpeg"))
imagenes += glob.glob(os.path.join(carpeta, "*.png"))

if len(imagenes) == 0:
    print("ERROR: No encontré ninguna imagen en la carpeta.")
    exit()

# Tomar la primera imagen encontrada
ruta = imagenes[0]

print("Imagen encontrada:")
print(ruta)

imagen = cv2.imread(ruta)

if imagen is None:
    print("No se pudo abrir la imagen")
    exit()

# Cambiar tamaño
imagen = cv2.resize(imagen, (800, 600))

# Escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Suavizar
gris = cv2.GaussianBlur(gris, (5, 5), 0)

# Convertir a blanco y negro
_, binaria = cv2.threshold(
    gris,
    120,
    255,
    cv2.THRESH_BINARY_INV
)

# Buscar contornos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

centros = []

for contorno in contornos:

    area = cv2.contourArea(contorno)

    if area > 1000:

        x, y, w, h = cv2.boundingRect(contorno)

        cx = x + w // 2
        cy = y + h // 2

        centros.append((cx, cy))

        # Rectángulo verde
        cv2.rectangle(
            imagen,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Centro rojo
        cv2.circle(
            imagen,
            (cx, cy),
            6,
            (0, 0, 255),
            -1
        )

# Ordenar objetos de izquierda a derecha
centros = sorted(centros, key=lambda p: p[0])

print("Objetos detectados:", len(centros))

if len(centros) >= 2:

    x1, y1 = centros[0]
    x2, y2 = centros[1]

    distancia = math.sqrt(
        (x2 - x1)**2 +
        (y2 - y1)**2
    )

    # Línea azul
    cv2.line(
        imagen,
        (x1, y1),
        (x2, y2),
        (255, 0, 0),
        3
    )

    # Punto medio
    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2

    cv2.putText(
        imagen,
        f"Distancia: {distancia:.2f} px",
        (mx - 100, my - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 0, 0),
        2
    )

    print(f"Distancia entre objetos: {distancia:.2f} pixeles")

else:

    print("No se detectaron dos objetos.")

# Mostrar resultados
cv2.imshow("Objetos detectados", imagen)
cv2.imshow("Imagen binaria", binaria)

cv2.waitKey(0)
cv2.destroyAllWindows()
