def status_lulus(nilai):
    if nilai >= 60:  # Perbaikan di sini (menggunakan >=)
        return "Lulus"
    return "Tidak lulus"


for n in [75, 60, 59]:
    print(n, "->", status_lulus(n))