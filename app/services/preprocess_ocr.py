import cv2
import pytesseract
from app.core.config import OCR_LANG, OCR_CONFIG

def run_ocr(img):
    if img is None:
        raise ValueError("Image invalid")

    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    median = cv2.medianBlur(gray, 5)

    kernel_bg = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opened_bg = cv2.morphologyEx(median, cv2.MORPH_OPEN, kernel_bg)

    _, thresh = cv2.threshold(
        opened_bg, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    text = pytesseract.image_to_string(
        thresh,
        lang=OCR_LANG,
        config=OCR_CONFIG
    )

    return text
