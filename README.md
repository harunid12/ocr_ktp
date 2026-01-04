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

## Instalasi Proyek
### 1. Clone Repository
```bash

git clone https://github.com/harunid12/ocr_ktp.git
cd ocr_ktp
```

### 2. Buat dan Aktifkan Virtual Environment
### Windows
```cmd

python -m venv venv
venv\Scripts\activate
```

### Linux/macOS
```bash

python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependecies
```bash
pip install -r requirements.txt
```


## Menjalankan Aplikasi 
```bash
uvicorn app.main:app --reload
```

Aplikasi Berjalan pada 
```text
http://127.0.0.1:8000
```

Dokumentasi API 
```text
http://127.0.0.1:8000/docs
```

## Alur Kerja Sistem
1. Client mengirimkan gambar KTP melalui endpoint API
2. Gambar diproses pada layer utilitas (preprocessing)
3. OCR dilakukan menggunakan Tesseract
4. Hasil OCR diproses dan dibersihkan dari whitespace berlebih
5. Data diparsing menjadi field KTP terstruktur
6. Response dikembalikan dalam format JSON

## Batasan
1. Akurasi OCR bergantung pada kualitas gambar
2. Pencahayaan dan resolusi rendah dapat mempengaruhi hasil ekstraksi
3. Format KTP non-standar dapat menurunkan akurasi parsing

## Author
### Ahmad Harun
AI Engineer

## Lisensi
Proyek ini dibuat untuk keperluan pembelajaran dan pengembangan sistem OCR. Penggunaan dan modifikasi diperbolehkan sesuai kebutuhan.
