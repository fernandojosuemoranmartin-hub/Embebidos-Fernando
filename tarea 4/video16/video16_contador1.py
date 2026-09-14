import cv2

# Leer imagen
imagen = cv2.imread("monedas.jpg")

if imagen is None:
    print("Error: No se encontro monedas.jpg")
    exit()

# Convertir a escala de grises
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralizacion
_, binaria = cv2.threshold(
    grises,
    240,
    255,
    cv2.THRESH_BINARY_INV
)

# Buscar contornos externos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Fuente para escribir texto
fuente = cv2.FONT_HERSHEY_SIMPLEX

contador = 0

for contorno in contornos:

    # Calcular el area para evitar ruido
    area = cv2.contourArea(contorno)

    if area > 500:

        contador += 1

        # Calcular momentos del contorno
        M = cv2.moments(contorno)

        if M["m00"] != 0:
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])

            # Escribir numero del objeto
            cv2.putText(
                imagen,
                "Num: " + str(contador),
                (x - 40, y),
                fuente,
                0.7,
                (255, 0, 0),
                2
            )

            # Dibujar contorno
            cv2.drawContours(
                imagen,
                [contorno],
                -1,
                (0, 0, 255),
                3
            )

# Mostrar cantidad total
print("Objetos encontrados:", contador)

# Mostrar ventanas
cv2.imshow("Imagen binaria", binaria)
cv2.imshow("Objetos contados", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()
