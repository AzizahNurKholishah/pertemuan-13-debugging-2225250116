# Pertemuan 13 - Debugging dan Testing

- **Nama:** Azizah Nur Kholishah
- **NIM:** 2225250116
- **Kelas:** 3-E

## Kasus
Program yang diuji adalah program pemrosesan nilai mahasiswa (praktik/praktik_4_debugging.py) yang terdiri dari tiga fungsi utama:
1. `hitung_rata_rata(nilai)` untuk menghitung nilai rata-rata.
2. `status(nilai)` untuk menentukan kelulusan (Lulus / Tidak lulus).
3. `nilai_tertinggi(nilai)` untuk mencari nilai maksimum dari sekumpulan data.

Program ini berjalan tanpa syntax error, namun mengandung beberapa logical error dan belum menangani kondisi khusus (seperti list kosong atau angka negatif) sehingga menghasilkan output yang salah.

## Test Case
| ID | Target / Input | Expected | Actual Awal | Status |
| :---: | :--- | :---: | :---: | :---: |
| **T1** | rata-rata: `[80, 60, 90, 70]` | `75.0` | `60.0` | **FAIL** |
| **T2** | rata-rata: `[100, 80]` | `90.0` | `36.0` | **FAIL** |
| **T3** | status: `60` | `Lulus` | `Tidak lulus` | **FAIL** |
| **T4** | status: `59` | `Tidak lulus` | `Tidak lulus` | **PASS** |
| **T5** | tertinggi: `[80, 60, 90, 70]` | `90` | `0` | **FAIL** |
| **T6** | rata-rata kosong: `[]` | `0` | `ZeroDivisionError` | **FAIL** |
| **T7** | tertinggi kosong: `[]` | `None` | `0` | **FAIL** |
| **T8** | tertinggi negatif: `[-5, -2, -9]` | `-2` | `0` | **FAIL** |

## Bug Report
| Bug ID | Gejala | Lokasi | Akar Penyebab | Perbaikan | Retest |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **B01** | Rata-rata `[80, 60, 90, 70]` bernilai `60.0`, bukan `75.0`. | `hitung_rata_rata`, `return sum(nilai) / 5` | Pembagi ditulis tetap 5, sehingga hanya benar jika datanya tepat 5. | Pembagi diganti menggunakan `len(nilai)`, ditambah penanganan list kosong agar terhindar dari pembagian nol. | **PASS** |
| **B02** | Nilai `60` dianggap "Tidak lulus". | `status`, `if nilai > 60` | Operator perbandingan menggunakan `>` sehingga mengecualikan nilai tepat di batas. | Mengubah operator perbandingan dari `>` menjadi `>=`. | **PASS** |
| **B03** | Nilai tertinggi selalu 0 atau salah pada data negatif. | `nilai_tertinggi`, `if x < tertinggi` | Logika perbandingan terbalik (`x < tertinggi`) dan inisialisasi awal `tertinggi = 0`. | Inisialisasi awal diambil dari `nilai[0]`, perulangan dari `nilai[1:]`, dan operator diubah menjadi `x > tertinggi`. | **PASS** |

## Retest
| ID | Target | Input / Kondisi | Expected | Actual Retest | Status Akhir |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **T1** | rata-rata | `[80, 60, 90, 70]` | `75.0` | `75.0` | **PASS** |
| **T2** | rata-rata | `[100, 80]` | `90.0` | `90.0` | **PASS** |
| **T3** | status | `60` | `Lulus` | `Lulus` | **PASS** |
| **T4** | status | `59` | `Tidak lulus` | `Tidak lulus` | **PASS** |
| **T5** | tertinggi | `[80, 60, 90, 70]` | `90` | `90` | **PASS** |
| **T6** | rata-rata kosong | `[]` | `0` | `0` | **PASS** |
| **T7** | tertinggi kosong | `[]` | `None` | `None` | **PASS** |
| **T8** | tertinggi negatif | `[-5, -2, -9]` | `-2` | `-2` | **PASS** |

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi
Teknik *debugging* yang paling membantu adalah menggunakan *breakpoint* pada VS Code karena kita bisa memantau jalannya program dan perubahan nilai variabel secara langsung pada setiap baris kode. Hal ini membuat pencarian *logical error* menjadi jauh lebih cepat, efektif, dan akurat dibandingkan harus menebak-nebak letak kesalahannya.

## Exit Ticket
- **Teknik debugging yang paling membantu saya hari ini adalah** Menggunakan breakpoint dan panel Variables pada VS Code, karena kita dapat memantau jalannya program serta melihat perubahan nilai variabel secara langsung baris demi baris secara transparan.
- **Bug logika lebih sulit daripada syntax error karena** Program tetap dapat berjalan lancar tanpa menimbulkan pesan error atau exception, namun memberikan hasil perhitungan atau logika yang salah secara senyap sehingga lebih sulit dideteksi tanpa pengujian yang teliti.
- **Test case batas yang baik untuk program nilai adalah** Pengujian pada nilai tepat di ambang batas kelulusan (seperti angka 60), di bawah batas (seperti angka 59), list kosong ([]), serta pengujian menggunakan data angka negatif untuk memastikan fungsi menangani kondisi ekstrem dengan benar.
- **Kebiasaan debugging yang akan saya bawa ke proyek pertemuan 14 adalah** Merancang test case terlebih dahulu (termasuk edge-case dan kondisi kosong) serta melakukan pengujian otomatis secara berkala setiap kali selesai memperbaiki atau menambah kode program.