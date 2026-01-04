# KTP OCR API menggunakan FastAPI dan Tesseract

Proyek ini merupakan REST API untuk melakukan **Optical Character Recognition (OCR)** pada **KTP Indonesia** menggunakan **Tesseract OCR**, **OpenCV**, dan **FastAPI**. Sistem dirancang secara modular untuk memisahkan logika API, service, utilitas, dan konfigurasi sehingga mudah dikembangkan dan dipelihara.

## Fitur

- OCR KTP Indonesia berbasis Tesseract
- Preprocessing citra untuk meningkatkan akurasi OCR
- Parsing hasil OCR menjadi data KTP terstruktur (JSON)
- REST API menggunakan FastAPI
- Arsitektur modular dan scalable
- Mendukung virtual environment (venv)
- Manajemen dependensi melalui `requirements.txt`

## Struktur Proyek

```text
ktp-ocr-api/
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── api/
│   │   └── routes/
│   │       └── ocr.py
│   ├── services/
│   │   ├── ktp_parser.py
│   │   └── preprocess_ocr.py
│   ├── utils/
│   │   └── image_utils.py
│   └── __init__.py
├── venv/
├── requirements.txt
├── README.md
└── .gitignore
```


## Prasyarat

- Python 3.9 atau lebih baru
- Tesseract OCR Engine
- Windows atau Linux

### Instalasi Tesseract

**Windows**
- Unduh dari: https://github.com/UB-Mannheim/tesseract/wiki
- Tambahkan path Tesseract ke environment variable `PATH`

**Linux**
```bash
sudo apt update
sudo apt install tesseract-ocr

```



