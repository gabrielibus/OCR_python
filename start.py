from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('./example.jpeg')
texto = pytesseract.image_to_string(image)

print(texto)

