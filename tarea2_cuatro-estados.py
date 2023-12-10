# importaion de las bibliotecas
import numpy as np
import cv2
import os

# funcion para importar una imagen
def cargarImagen():
    ruta = os.getcwd()
    nombreImagen = r'resources/tiger.jpg'
    rutaAbrir = os.path.join(ruta, nombreImagen)
    imagen = cv2.imread(rutaAbrir)
    
    cv2.imshow('img',imagen)
    cv2.moveWindow('img',0,0)
    
    return imagen

def TrasladarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape
    
    M = np.float32([[1,0,25], [0, 1, 50]])
    imgT1 = cv2.warpAffine(img, M, (w, h))
    
    cv2.imshow("imgT1", imgT1)
    cv2.moveWindow("imgT1",w,0)
    return imgT1

def RotarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape
    
    centro = (int(w//2), int(h//2))
    angulo = 90
    escala = 1
    
    M = cv2.getRotationMatrix2D(centro, angulo, escala)
    imgR1 = cv2.warpAffine(img, M, (w, h))
    
    cv2.imshow("imgR1", imgR1)
    cv2.moveWindow("imgR1",2*w,0)
    
    return imgR1

def EscalarImagen(imagen):
    img = imagen.copy()
    h, w, c = img.shape

    #cambiar de tamaño
    rFactor = 0.5
    tamano = (int(rFactor*w), int(rFactor*h))

    imgE1 = cv2.resize(img, tamano)
  
    cv2.imshow("imgE1", imgE1)
    cv2.moveWindow("imgE1", 3*w, 0)

    return imgE1

def cizallarImagen(imagen, shear_factor):
    img = imagen.copy()
    h, w, c = img.shape
    
    shear_matrix = np.array([[1, shear_factor, 0],
                             [0, 1, 0]], dtype=np.float32)
    sheared_imagen = cv2.warpAffine(imagen, shear_matrix, (w, h))
    
    cv2.imshow("imgC1", sheared_imagen)
    cv2.moveWindow("imgC1", 3*w, 0)

    return sheared_imagen

def aplicar_transparencia(imagen, alpha):
    img = imagen.copy()
    transparente = np.zeros_like(img, dtype=np.uint8)
    imagen_transparente = cv2.addWeighted(img, 1 - alpha, transparente, alpha, 0)
    cv2.imshow("imgTR1", imagen_transparente)

    return imagen_transparente

if __name__ == "__main__":
    img = cargarImagen()
    TrasladarImagen(img)
    RotarImagen(img)
    EscalarImagen(img)
    cizallarImagen(img, 0.5)
    aplicar_transparencia(img, 0.5)
    cv2.waitKey(0)