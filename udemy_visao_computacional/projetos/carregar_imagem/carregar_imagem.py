#   EXERCÍCIO REALIZADO SEGUINDO VÍDEO AULA
#   IMPORTAÇÃO DO OPENCV
import cv2 as cv

#   IMPORTAÇÃO DA IMAGEM E CONVERSÕES
imagem = cv.imread('udemy_visao_computacional\Images\people1.jpg')    #IMPORTANDO IMAGEM
img = cv.resize(imagem, (800, 600))                          #REDIMENSIONANDO IMAGEM PARA 800X600 PIXELS
imagem  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                #CONVERTENDO PARA ESCALA DE CINZA (CANAL ÚNICO)

#   JANELA PARA EXIBIR A IMAGEM
cv.namedWindow('imagem')
cv.imshow('imagem', imagem) 
cv.waitKey()

'''
    Sempre utilizar desta maneira quando for exibir a imagem no terminal,
    para garantir que será exibida até que um tecla seja pressionada no teclado.

'''