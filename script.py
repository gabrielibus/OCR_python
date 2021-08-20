from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file = input('Por favor arrastre la imagen a esta ventana para procesarla: ')
file = (file.split('"')[1])
image = Image.open(file)
texto = pytesseract.image_to_string(image, lang='eng')

print(texto,"\n\n")

