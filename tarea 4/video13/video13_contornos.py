import cv2

# Leer la imagen
imagen = cv2.imread("figContorno.png")

if imagen is None:
    print("Error: No se encontro la imagen figContorno.png")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria
_, binaria = cv2.threshold(
    gris,
    100,
    255,
    cv2.THRESH_BINARY
)

# Encontrar contornos externos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar todos los contornos encontrados
cv2.drawContours(
    imagen,
    contornos,
    -1,
    (0, 255, 0),
    3
)

# Mostrar numero de contornos
print("Numero de contornos encontrados:", len(contornos))

# Mostrar resultados
cv2.imshow("Imagen binaria", binaria)
cv2.imshow("Contornos", imagen)

print("Presiona cualquier tecla para salir")

cv2.waitKey(0)
cv2.destroyAllWindows()
