from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

testImg1 = Image.open("./imgs/test-receipt-1.jpg")
testImg2 = Image.open("./imgs/test-receipt-2.jpg")
testImg3 = Image.open("./imgs/test-receipt-3.jpg")
testImg4 = Image.open("./imgs/test-receipt-4.jpg")

# print(pytesseract.image_to_string(testImg1))
# print(pytesseract.image_to_string(testImg2))
#print(pytesseract.image_to_string(testImg3))
print(pytesseract.image_to_string(testImg4))