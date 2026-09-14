import cv2
import numpy as np


# Funcion para dibujar y numerar los contornos
def dibujar_contornos(imagen, contornos, color):

    contador = 0

    for contorno in contornos:

        area = cv2.contourArea(contorno)

        # Evitar objetos demasiado pequeños
        if area > 500:

            contador += 1

            M = cv2.moments(contorno)

            if M["m00"] != 0:

                x = int(M["m10"] / M["m00"])
                y = int(M["m01"] / M["m00"])

                # Dibujar contorno
                cv2.drawContours(
                    imagen,
                    [contorno],
                    -1,
                    color,
                    3
                )

                # Escribir numero
                cv2.putText(
                    imagen,
                    str(contador),
                    (x - 10, y + 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 0),
                    2
                )

    return contador


# ==========================================
# LEER IMAGEN
# ==========================================

imagen = cv2.imread("lunares.png")

if imagen is None:
    print("Error: No se encontro lunares.png")
    exit()


# Convertir de BGR a HSV
imagenHSV = cv2.cvtColor(
    imagen,
    cv2.COLOR_BGR2HSV
)


# ==========================================
# RANGOS DE COLORES
# ==========================================

# Amarillo
amarillo_bajo = np.array([20, 100, 20], np.uint8)
amarillo_alto = np.array([32, 255, 255], np.uint8)

# Violeta
violeta_bajo = np.array([130, 100, 20], np.uint8)
violeta_alto = np.array([145, 255, 255], np.uint8)

# Verde
verde_bajo = np.array([36, 100, 20], np.uint8)
verde_alto = np.array([70, 255, 255], np.uint8)

# Rojo - primer rango
rojo_bajo1 = np.array([0, 100, 20], np.uint8)
rojo_alto1 = np.array([10, 255, 255], np.uint8)

# Rojo - segundo rango
rojo_bajo2 = np.array([175, 100, 20], np.uint8)
rojo_alto2 = np.array([179, 255, 255], np.uint8)


# ==========================================
# CREAR MASCARAS
# ==========================================

mascara_amarillo = cv2.inRange(
    imagenHSV,
    amarillo_bajo,
    amarillo_alto
)

mascara_violeta = cv2.inRange(
    imagenHSV,
    violeta_bajo,
    violeta_alto
)

mascara_verde = cv2.inRange(
    imagenHSV,
    verde_bajo,
    verde_alto
)

mascara_rojo1 = cv2.inRange(
    imagenHSV,
    rojo_bajo1,
    rojo_alto1
)

mascara_rojo2 = cv2.inRange(
    imagenHSV,
    rojo_bajo2,
    rojo_alto2
)

# Unir los dos rangos del rojo
mascara_rojo = cv2.add(
    mascara_rojo1,
    mascara_rojo2
)


# ==========================================
# ENCONTRAR CONTORNOS
# ==========================================

contornos_amarillo, _ = cv2.findContours(
    mascara_amarillo,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contornos_violeta, _ = cv2.findContours(
    mascara_violeta,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contornos_verde, _ = cv2.findContours(
    mascara_verde,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contornos_rojo, _ = cv2.findContours(
    mascara_rojo,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


# ==========================================
# DIBUJAR Y CONTAR
# ==========================================

amarillos = dibujar_contornos(
    imagen,
    contornos_amarillo,
    (0, 255, 255)
)

violetas = dibujar_contornos(
    imagen,
    contornos_violeta,
    (140, 40, 120)
)

verdes = dibujar_contornos(
    imagen,
    contornos_verde,
    (0, 255, 0)
)

rojos = dibujar_contornos(
    imagen,
    contornos_rojo,
    (0, 0, 255)
)


# Total
total = amarillos + violetas + verdes + rojos


# Mostrar resultados en terminal
print("Amarillos:", amarillos)
print("Violetas:", violetas)
print("Verdes:", verdes)
print("Rojos:", rojos)
print("Total de objetos:", total)


# ==========================================
# IMAGEN RESUMEN
# ==========================================

resumen = 255 * np.ones(
    (250, 250, 3),
    dtype=np.uint8
)

cv2.putText(
    resumen,
    "CONTEO",
    (60, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 0, 0),
    2
)

cv2.circle(resumen, (30, 70), 15, (0, 255, 255), -1)
cv2.putText(resumen, str(amarillos), (60, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

cv2.circle(resumen, (30, 110), 15, (140, 40, 120), -1)
cv2.putText(resumen, str(violetas), (60, 120),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

cv2.circle(resumen, (30, 150), 15, (0, 255, 0), -1)
cv2.putText(resumen, str(verdes), (60, 160),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

cv2.circle(resumen, (30, 190), 15, (0, 0, 255), -1)
cv2.putText(resumen, str(rojos), (60, 200),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

cv2.putText(
    resumen,
    "Total: " + str(total),
    (30, 235),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (0, 0, 0),
    2
)


# Mostrar ventanas
cv2.imshow("Objetos por color", imagen)
cv2.imshow("Resumen", resumen)

cv2.waitKey(0)
cv2.destroyAllWindows()
