
#arquivo txt para corte de peças#
import cv2
import numpy as np

imagemcaixa= "CaixaC513.jpg"

image =cv2.imread(imagemcaixa)
#cv2.imshow("caixa de macha",image)
#cv2.waitKey(0)
import cv2

imagem = cv2.imread('caixac513.jpg')
#Cria um retangulo azul por toda a largura da imagem
image[590:600, 200:500] = (255, 0, 0)#fazlinhas na horizontal
image[490:500, 200:500] = (255, 0, 0)#fazlinhas na horizontal
image[500:600, 200:210] = (255, 0, 0)#faz linha na vertical
image[500:600, 490:500] = (255, 0, 0)#faz linha na vertical

import cv2
imagem = cv2.imread('caixac513.jpg')
recorte = imagem[490:600, 200:500]#faz recorte
cv2.imshow("Recorte da imagem", recorte)
cv2.imwrite("recorte.jpg", recorte) #salva no disco

cv2.imshow("Imagem modificada", image)
cv2.waitKey(0)


