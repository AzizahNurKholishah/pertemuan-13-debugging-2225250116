def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

tests = [
    ("T1", [80, 90, 70], 80.0),
    ("T2", [100, 80], 90.0),
    ("T3", [70, 70, 70], 70.0),
    ("T4", [], 0),
]

for kode, masukan, harapan in tests:
    hasil = rata_rata(masukan)
    status_uji = "PASS" if hasil == harapan else "FAIL"
    print(f"{kode} | Input: {masukan} | Expected: {harapan} | Actual: {hasil} | Status: {status_uji}")