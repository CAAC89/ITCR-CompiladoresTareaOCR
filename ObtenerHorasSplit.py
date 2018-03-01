import pytesseract
import os
import re
from PIL import Image

directorio= os.path.join(os.path.expanduser("~"),"Downloads","7001-ALA-HER.png")
imagen=Image.open(directorio)
texto_imagen=pytesseract.image_to_string(imagen)

with open("salida_horarios.txt",mode ="w")as file:
    file.write(texto_imagen)
archivo=open("salida_horarios.txt",mode="r")
patron_horas=re.compile("([01][0-9]|2[0-3])(:)([0-5][0-9])")
horario=[]
for linea in archivo:
    fila_horas=[]
    if patron_horas.match(linea):
        fila_horas+=(linea.rstrip()).split()
        horario+=[fila_horas]
print (horario)
