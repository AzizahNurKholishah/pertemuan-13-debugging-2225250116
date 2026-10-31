"""Kasus 3: Membaca nilai dari file. 
Program gagal pada file kosong / tidak ada / data tidak valid.
Tugas: baca traceback, tentukan jenis exception, lalu rancang penanganannya.
"""

import os
import tempfile


def rata_rata_file(nama_file):
    try:
        with open(nama_file, "r") as f:
            # Mengonversi setiap baris file menjadi integer
            nilai = [int(baris.strip()) for baris in f]
            
        # Penanganan jika list kosong (file kosong) untuk menghindari ZeroDivisionError
        if len(nilai) == 0:
            return "ERROR: File kosong, tidak ada data untuk dihitung."
            
        return sum(nilai) / len(nilai)

    except FileNotFoundError:
        return "ERROR: File tidak ditemukan di direktori."
    except ValueError as e:
        return f"ERROR: Data di dalam file tidak valid (ditemukan teks/non-angka) -> {e}"
    except ZeroDivisionError:
        return "ERROR: Terjadi pembagian dengan nol."


def coba(label, nama_file):
    print(label, "->", rata_rata_file(nama_file))


# --- Simulasi Pengujian Kasus 3 ---
# Membuat folder sementara untuk pengujian file
folder = tempfile.mkdtemp()
file_ada = os.path.join(folder, "nilai.txt")
file_kosong = os.path.join(folder, "kosong.txt")
file_rusak = os.path.join(folder, "rusak.txt")

# Mengisi file normal
with open(file_ada, "w") as f:
    f.write("80\n90\n70\n")

# Membiarkan file kosong
open(file_kosong, "w").close()

# Mengisi file dengan data rusak / teks huruf
with open(file_rusak, "w") as f:
    f.write("80\nabc\n70\n")

# Menjalankan pengujian untuk setiap skenario error
coba("file normal", file_ada)
coba("file kosong", file_kosong)
coba("data tidak valid", file_rusak)
coba("file tidak ada", os.path.join(folder, "tidak_ada.txt"))