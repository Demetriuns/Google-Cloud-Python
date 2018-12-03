import io
import os

import cv2
import time

# Método de acesso a câmera e registro da imagem capturada 
def main(args):

    camera_port = 0
  
    nFrames = 30
  
    camera = cv2.VideoCapture(camera_port)
     
    file = "-Patch-"
         
    print ("Digite <ESC> para sair / <s> para Salvar")
     
    emLoop= True
      
    while(emLoop):
     
        retval, img = camera.read()
        cv2.imshow('Foto',img)
     
        k = cv2.waitKey(100)
     
        if k == 27:
            emLoop= False
         
        elif k == ord('s'):
            cv2.imwrite(file,img)
            emLoop= False
     
    cv2.destroyAllWindows()
    camera.release()
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)
    
# Importando as bibliotecas do Google Cloud.
from google.cloud import vision
from google.cloud.vision import types

# Instanciando um cliente
client = vision.ImageAnnotatorClient()

# O arquivo de imagem para análise.
file_name = os.path.join(
    os.path.dirname(__file__),
    '-Patch-')

# Carregando a imagem na memória.
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Recebendo os Labels da imagem analisada.
response = client.label_detection(image=image)
labels = response.label_annotations

# Importando a fala do Windows.
import win32com.client as wincl

# Retornando a análise através da fala. 
print('Labels:')
for label in labels[:2]:
    print(label.description)
    print(label.score)
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(label.description)
    speak.Speak(int( label.score *100 ) )
    speak.Speak('por cento')
    
