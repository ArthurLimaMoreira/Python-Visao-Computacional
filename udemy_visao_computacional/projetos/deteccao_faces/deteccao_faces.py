#   EXERCÍCIO REALIZADO SEGUINDO VÍDEO AULA
#   IMPORTAÇÃO DO OPENCV
import cv2 as cv

#   IMPORTAÇÃO DA IMAGEM E CONVERSÕES
img = cv.imread('udemy_visao_computacional\Images\people1.jpg')    #IMPORTANDO IMAGEM
img = cv.resize(img, (800, 600))                          #REDIMENSIONANDO IMAGEM PARA 800X600 PIXELS
imagem  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                #CONVERTENDO PARA ESCALA DE CINZA (CANAL ÚNICO)


#   DETECCAO DAS FACES
detector = cv.CascadeClassifier('udemy_visao_computacional\cascades\haarcascade_frontalface_default.xml')   #busca arquivo .xml do classificador de faces

deteccao = detector.detectMultiScale(imagem)    #realiza a detecção das faces na imagem

# print(deteccao)                                 #mostra no terminal as corrdenadas XY das faces detectadas (início delas e tamanho da face detectada)

for x, y, w, h in deteccao:
    cv.rectangle(img, (x, y), (x + w, y + h),(0, 0, 255), 3)   #cria um ponto no pixel onde inicia cada face
    #   imagem, XY inicial, lados do retangulo, cor, espessura da borda    
    #print(x, y, w, h)

#   JANELA PARA EXIBIR A IMAGEM
cv.namedWindow('imagem')
cv.imshow('imagem', img)
cv.waitKey()
