import cv2

# Leer imagen
imagen = cv2.imread("cartas.jpg")

if imagen is None:
    print("Error: No se encontro cartas.jpg")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Suavizar imagen para reducir ruido
suavizada = cv2.GaussianBlur(gris, (5, 5), 0)

# Detectar bordes con Canny
bordes = cv2.Canny(
    suavizada,
    50,
    150
)

# Buscar contornos
contornos, _ = cv2.findContours(
    bordes,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contador = 0

for contorno in contornos:

    area = cv2.contourArea(contorno)

    # Evitar contar ruido pequeño
    if area > 1000:

        contador += 1

        # Dibujar contorno
        cv2.drawContours(
            imagen,
            [contorno],
            -1,
            (0, 0, 255),
            3
        )

        # Obtener rectangulo alrededor del objeto
        x, y, w, h = cv2.boundingRect(contorno)

        # Escribir numero del objeto
        cv2.putText(
            imagen,
            "Objeto " + str(contador),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

# Mostrar cantidad total
print("Objetos encontrados:", contador)

# Mostrar resultados
cv2.imshow("Bordes Canny", bordes)
cv2.imshow("Objetos detectados", imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()
