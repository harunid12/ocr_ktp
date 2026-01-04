from fastapi import FastAPI
from app.api.routes import ocr

app = FastAPI(
    title="KTP OCR",
    description="OCR & Parsing KTP Indonesia",
    version="1.0"
)

app.include_router(
    ocr.router,
    prefix="/ocr",
    tags=["OCR"]
)
