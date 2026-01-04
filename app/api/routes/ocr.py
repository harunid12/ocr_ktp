from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from app.utils.image_utils import bytes_to_cv2_image
from app.services.preprocess_ocr import run_ocr
from app.services.ktp_parser import parse_ktp

router = APIRouter()

@router.post("/proses")
async def ocr_ktp(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        return JSONResponse(
            status_code=400,
            content={"error": "File harus JPG atau PNG"}
        )

    image_bytes = await file.read()
    img = bytes_to_cv2_image(image_bytes)

    if img is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Gambar tidak valid"}
        )

    raw_text = run_ocr(img)
    data = parse_ktp(raw_text)

    return {
        "filename": file.filename,
        "raw_text": raw_text,
        "data": data
    }
