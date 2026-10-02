import cv2
import pytesseract
import os

# Ruta donde está instalado Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Obtener la carpeta donde está este archivo .py
carpeta = os.path.dirname(os.path.abspath(__file__))

# Buscar la imagen dentro de la carpeta video39
ruta_imagen = os.path.join(carpeta, "video39", "prueba.jpg")

print("Buscando imagen en:")
print(ruta_imagen)

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

if imagen is None:
    print("No se pudo cargar la imagen")
else:
    # Reconocer texto
    texto = pytesseract.image_to_string(imagen)

    print("\nTexto detectado:")
    print("----------------------")
    print(texto)

    # Mostrar imagen
    cv2.imshow("Imagen de prueba", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
