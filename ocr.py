import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from pdf2image import convert_from_bytes

# PDF dosyasını bayt olarak oku
with open("x.pdf", "rb") as f:
    pdf_bytes = f.read()

    # PDF'yi resimlere dönüştür (birden fazla sayfa olabilir)
    images = convert_from_bytes(pdf_bytes)

    # OCR yapılandırması (Tesseract için)
    custom_config = r'--oem 3 --psm 6'

    # Her sayfadaki metni OCR ile çöz ve birleştir
    pdf_txt = '\n\n'.join(
        pytesseract.image_to_string(image, config=custom_config)
        for image in images
    )

    # Gereksiz null karakterleri kaldır
    pdf_txt = pdf_txt.replace("\x00", " ")

# OCR'dan elde edilen metni yazdır
print(pdf_txt)