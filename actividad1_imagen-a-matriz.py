import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread(r"resources/tiger.jpg")

# Comprobar si la carga fue exitosa
if imagen is not None:
    print('La imagen se ha cargado correctamente en forma de matriz.')
else:
    print('No se pudo cargar la imagen.')

# Obtener las dimensiones de la imagen
alto, ancho, canales = imagen.shape

# Convertir la imagen en una matriz
matriz_imagen = imagen.reshape(alto, ancho * canales)

# Mostrar la matriz de la imagen
print('Matriz de la imagen:')
print(matriz_imagen)

# Convertir la matriz de nuevo en una imagen
imagen_recuperada = matriz_imagen.reshape(alto, ancho, canales)

# Mostrar la imagen recuperada
cv2.imshow("Imagen Recuperada", imagen_recuperada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar la matriz en un archivo de texto
np.savetxt('matriz_generada.txt', matriz_imagen, fmt='%d')

print('La matriz se ha guardado en un archivo de texto (matriz_generada.txt).')