"""Latihan 3 - Bug Batas Kelulusan
"""

def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


# Menjalankan pengujian otomatis dan membandingkan hasil
for kode, masukan, harapan in tests:
    hasil = status_lulus(masukan)
    status_uji = "PASS" if hasil == harapan else "FAIL"
    print(f"{kode} | Input: {masukan} | Expected: {harapan} | Actual: {hasil} | Status: {status_uji}")