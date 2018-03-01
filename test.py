import pytesseract
import os
from PIL import Image

directorio= os.path.join(os.path.expanduser("~"),"Downloads","7001-ALA-HER.png")
imagen=Image.open(directorio)
texto_imagen=pytesseract.image_to_string(imagen)

with open("salida_horarios.txt",mode ="w")as file:
    file.write(texto_imagen)
