import fitz
import pytesseract
from PIL import Image
import io 

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\RakeshRanjan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# def parse_pdf(file_bytes: bytes) -> list[str]:
#     pdf = fitz.open(stream=file_bytes, filetype="pdf")
#     text = ""
#     for page in pdf:
#         text += page.get_text()
#     return [text]
 
def parse_pdf(file_bytes: bytes) -> list[str]:
    pdf = fitz.open(stream=file_bytes, filetype="pdf")
    all_text = []
 
    for page in pdf:
        text = page.get_text().strip()
        if text:
            all_text.append(text)
        else:
            pix = page.get_pixmap(dpi=300)
            image = Image.open(io.BytesIO(pix.tobytes("png")))
            ocr_text = pytesseract.image_to_string(image)
            all_text.append(ocr_text)
 
    return all_text
 
 