import pytesseract
import os

# path tesseract engine
TESSERACT_PATH = os.getenv(
    "TESSERACT_PATH",
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

OCR_LANG = "ind"
OCR_CONFIG = "--oem 3 --psm 6"
