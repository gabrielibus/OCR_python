from PIL import Image
import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os

file = input('Por favor arrastre la imagen a esta ventana para procesarla: ')
image = Image.open(file)
texto = pytesseract.image_to_string(image, lang='eng')

texto_list = texto.split('\n')
fecha = ""
tipo = ""
secuencia = ""
last_linea = 0
first_linea = 0
sujetos = []
for i in range(len(texto_list)):
    linea = texto_list[i].lower()
    linea = re.sub(r'[^A-Za-z0-9\s]','', linea)
    if linea.count('acta') or linea.count('individual'):
        try:
            int(fecha[:2])
            fecha = linea.split(' ')[1]
            fecha = fecha[:2] + "-" + fecha[2:5] + "-" + fecha[5:10]
        except:
            pass
    if linea.count('grupo'):
        tipo = linea[20:].strip()
    if linea.count('repartido'):
        for i in linea.split(' '):
            if i.isdigit() and len(i) == 6:
                secuencia = i
        if fecha == "":
            fecha = (linea.split(" ")[-1])
            dia = fecha[:2] if fecha[:2].isdigit() else 'False'
            mes = fecha[2:-4].replace('0', 'o')
            year = fecha[-4:] if fecha[-4:].isdigit() else 'False'
            fecha = dia + "/" + mes + "/" + year
    if linea.count('apellido') or linea.count('sujeto') or linea.count('procesal') or linea.count('nombre'):
        first_linea = i + 1
    if linea.count('cuader') or linea.count('c27'):
        last_linea = i - 2

for i in range(len(texto_list)):
    if i >= first_linea and i <= last_linea:
            linea = texto_list[i][len(texto_list[i].split(" ")[0]) + 1:]
            linea = re.sub(r'[^A-Za-z0-9\s]','', linea)
            sujetos.append(linea)

print(secuencia)
print(fecha)
print(tipo)
print("\n".join(sujetos))

os.system('del temp')
os.system('echo ' + secuencia + " >> temp")
if not fecha == "":
    os.system('echo ' + fecha + ' >> temp')
os.system('echo ' + tipo + " >> temp")
for i in sujetos:
    os.system('echo ' + i + " >> temp")
os.system('clip < temp')

