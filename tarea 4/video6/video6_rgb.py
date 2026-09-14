import cv2
import numpy as np

# ==========================================
# PARTE 1: CREAR UNA IMAGEN CON NUMPY
# ==========================================

# Crear imagen negra de 500 x 800 pixeles
# El 3 representa los canales B, G y R
imagen = np.zeros((500, 800, 3), dtype=np.uint8)

# OpenCV trabaja los colores en orden BGR

# Azul
imagen[0:100, :] = (255, 0, 0)

# Verde
imagen[100:200, :] = (0, 255, 0)

# Rojo
imagen[200:300, :] = (0, 0, 255)

# Amarillo
imagen[300:400, :] = (0, 255, 255)

# Morado - cambio para experimentar
imagen[400:500, :] = (255, 0, 255)

# Agregar texto
fuente = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(imagen, "AZUL BGR = (255,0,0)",
            (20, 60), fuente, 0.8, (255, 255, 255), 2)

cv2.putText(imagen, "VERDE BGR = (0,255,0)",
            (20, 160), fuente, 0.8, (255, 255, 255), 2)

cv2.putText(imagen, "ROJO BGR = (0,0,255)",
            (20, 260), fuente, 0.8, (255, 255, 255), 2)

cv2.putText(imagen, "AMARILLO BGR = (0,255,255)",
            (20, 360), fuente, 0.8, (0, 0, 0), 2)

cv2.putText(imagen, "MORADO BGR = (255,0,255)",
            (20, 460), fuente, 0.8, (255, 255, 255), 2)

# Mostrar resultado
cv2.imshow("Colores en OpenCV - BGR", imagen)

print("OpenCV utiliza el orden BGR")
print("Presiona cualquier tecla para terminar")

cv2.waitKey(0)
cv2.destroyAllWindows()
