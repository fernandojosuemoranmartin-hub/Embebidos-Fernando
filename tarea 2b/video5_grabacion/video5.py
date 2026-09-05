import cv2

# Abrir la camara
camara = cv2.VideoCapture(0)

# Verificar que la camara se haya abierto
if not camara.isOpened():
    print("Error: No se pudo abrir la camara")
    exit()

# Obtener dimensiones de la camara
ancho = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Codec para guardar en formato MP4
codec = cv2.VideoWriter_fourcc(*'mp4v')

# Crear archivo de video
video = cv2.VideoWriter(
    "video_grabado.mp4",
    codec,
    20.0,
    (ancho, alto)
)

print("Grabando video...")
print("Presiona la tecla q para detener la grabacion.")

while True:

    # Capturar un frame
    ret, frame = camara.read()

    if not ret:
        print("No se pudo capturar el video")
        break

    # Mostrar video en pantalla
    cv2.imshow("Grabando video", frame)

    # Guardar frame en el archivo MP4
    video.write(frame)

    # Presionar q para terminar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Liberar camara y archivo
camara.release()
video.release()

# Cerrar ventanas
cv2.destroyAllWindows()

print("Video guardado como video_grabado.mp4")
