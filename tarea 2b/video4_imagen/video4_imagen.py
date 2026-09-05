import cv2

# Leer la imagen
imagen = cv2.imread("imagen.png")

# Verificar que se haya encontrado
if imagen is None:
    print("No se pudo encontrar la imagen.")
    exit()

# Mostrar imagen
cv2.imshow("Imagen Original", imagen)

# Guardar en formato JPEG
cv2.imwrite("imagen_guardada.jpeg", imagen)

print("Imagen guardada correctamente como JPEG")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
