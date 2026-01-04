import re

def normalize_text_global(text):
    text = text.upper()
    text = text.replace("’", "'").replace("`", "'")

    # hapus karakter aneh
    text = re.sub(r"[^A-Z0-9\s:/\-,.'\n]", "", text)

    text = re.sub(r"\s+", " ", text)  
    text = text.replace(" \n", "\n")
    text = text.replace("\n ", "\n")

    return text.strip()



OCR_FIX = {
    "O": "0",
    "I": "1",
    "L": "1",
    "S": "5",
    "B": "8",
    "Z": "2"
}

def normalize_number(text):
    for k, v in OCR_FIX.items():
        text = text.replace(k, v)
    return text


def clean_nik(text):
    if not text:
        return None

    # buang semua kecuali angka + huruf mirip angka
    text = re.sub(r"[^0-9OILSBZ]", "", text)
    text = normalize_number(text)

    return text[:16] if len(text) >= 16 else None


def clean_name(text):
    if not text:
        return None
    return re.sub(r"[^A-Z\s]", "", text).strip()


def clean_address(text):
    if not text:
        return None
    return re.sub(r"[^A-Z0-9\s./]", "", text).strip()


def clean_date(text):
    if not text:
        return None
    return re.sub(r"[^0-9\-]", "", text)


def parse_ktp(text):
    raw = normalize_text_global(text)

    def find(pattern):
        m = re.search(pattern, raw)
        if not m:
            return None

        value = m.group(1)
        value = value.strip()

        return value if value else None


    data = {
        "Provinsi": clean_name(find(r'PROVINSI\s+([A-Z ]+)')),
        "Kota": clean_name(find(r'\n([A-Z ]+)\n\s*NIK')),
        "NIK": clean_nik(find(r'NIK\s*:\s*([A-Z0-9\.,\'"/\- ]+)')),
        "Nama": clean_name(find(r'NAMA\s*:\s*([A-Z\s]+)')),
        "Tempat_Lahir": None,
        "Tanggal_Lahir": None,
        "Jenis_Kelamin": None,
        "Gol_Darah": None,
        "Alamat": clean_address(find(r'ALAMAT\s*:\s*([A-Z0-9\s./]+)')),
        "RT_RW": find(r'RT/RW\s*:\s*([0-9]{3}/[0-9]{3})'),
        "Kelurahan": clean_name(find(r'KEL/DESA\s*:\s*([A-Z ]+)')),
        "Kecamatan": clean_name(find(r'KECAMATAN\s*:\s*([A-Z ]+)')),
        "Agama": clean_name(find(r'AGAMA\s*:\s*([A-Z\s]+)')),
        "Status_Perkawinan": clean_name(find(r'STATUS PERKAWINAN\s*:\s*([A-Z ]+)')),
        "Pekerjaan": clean_name(find(r'PEKERJAAN\s*:\s*([A-Z\s]+)')),
        "Kewarganegaraan": clean_name(find(r'KEWARGANEGARAAN\s*:\s*([A-Z ]+)')),
        "Berlaku_Hingga": clean_date(find(r'BERLAKU HINGGA\s*:\s*([0-9\-]+)'))
    }

    ttl = re.search(
        r'TEMPAT.*LAHIR\s*:\s*([A-Z ]+),\s*([0-9\-]+)',
        raw
    )
    if ttl:
        data["Tempat_Lahir"] = clean_name(ttl.group(1))
        data["Tanggal_Lahir"] = clean_date(ttl.group(2))

    jk = re.search(
        r'JENIS KELAMIN\s*:\s*(LAKI-LAKI|PEREMPUAN)\s*GOL\s*DARAH\s*:\s*([A-Z])',
        raw
    )
    if jk:
        data["Jenis_Kelamin"] = jk.group(1)
        data["Gol_Darah"] = jk.group(2)

    return data
