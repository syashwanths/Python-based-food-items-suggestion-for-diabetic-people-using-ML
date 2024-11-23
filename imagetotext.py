import pytesseract
# import  re
# import pandas as pd
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'C:\foodlabel.jpeg'))


# # Assuming the extracted text has a table structure

# df = pd.DataFrame([line.split('\t') for line in extracted_text.splitlines()])  # Assuming tab-delimited columns

# product_id = 123
# specific_line = df[df['Product ID'] == product_id]

# if not specific_line.empty:
#     # Access values from the filtered DataFrame
#     price = specific_line['Price'].iloc[0]  # Assuming price is in a column named "Price"
#     print(f"Found line with Product ID {product_id}: Price = ${price}")
# else:
#     print(f"Line with Product ID {product_id} not found")