import cv2
import os

def transformar(arquivo, filtro):
    img = cv2.imread(f'fotos/{arquivo}')
    img_pb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invertida = cv2.bitwise_not(img_pb)
    img_blur = cv2.GaussianBlur(img_invertida, (filtro,filtro), 0)
    img_blur_invertida = cv2.bitwise_not(img_blur)
    img_desenho = cv2.divide(img_pb, img_blur_invertida, scale= 256.0)

    cv2.imwrite(f'desenho/{arquivo}', img_desenho)

lista_arquivos = os.listdir('fotos')

for arquivo in lista_arquivos:
    transformar(arquivo, 55)
