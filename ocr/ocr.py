import easyocr
import os

def perform_ocr(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    extracted_text = " ".join([text[1] for text in result])
    
    try:
        os.remove(image_path)
    except OSError as e:
        print(f"Error deleting the image {image_path}: {e.strerror}")
    
    return extracted_text