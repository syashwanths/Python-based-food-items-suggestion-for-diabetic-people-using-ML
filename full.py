import pytesseract
import re
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
text = pytesseract.image_to_string(Image.open('rg.jpg'))
cleaned_text = re.sub(r'(\d+)\s*(  |g|mg)', r'\1',text)

with open ('output.txt','w') as file:
    file.write(cleaned_text)
print("The text is written to file successfully")