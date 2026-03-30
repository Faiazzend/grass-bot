import pytesseract

def read_text(image):
    return pytesseract.image_to_string(image)