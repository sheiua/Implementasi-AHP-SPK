# Studi Kasus Metode AHP  
## Pemilihan HP Terbaik

---

# Contoh Kasus

Saya ingin membeli HP yang:

- Harganya relatif murah
- Memorinya besar
- Warnanya banyak
- Ukuran piksel kamera besar
- Beratnya ringan
- Bentuknya unik

Terdapat 4 alternatif HP:

1. N70  
2. N73  
3. N80  
4. N90  

---

# Pembahasan Metode AHP

# Tahap 1 — Identifikasi Masalah dan Menentukan Solusi

Terdapat 3 tahap identifikasi:

## Tujuan
Memilih HP terbaik sesuai kebutuhan pengguna.

## Kriteria
- Harga
- Memori
- Warna
- Kamera
- Berat
- Keunikan

## Alternatif
- N70
- N73
- N80
- N90

---

# Tahap 2 — Menyusun Hierarki

```text
                 TUJUAN
            Membeli HP Terbaik
                      │
 ┌────────┬────────┬────────┬────────┬────────┬────────┐
 Harga   Memori   Warna   Kamera   Berat   Keunikan
    │        │        │        │        │        │
 ───────────────────────────────────────────────────
    │        │        │        │        │        │
 N70      N70      N70      N70      N70      N70
 N73      N73      N73      N73      N73      N73
 N80      N80      N80      N80      N80      N80
 N90      N90      N90      N90      N90      N90
```

---

# Tahap 3 — Membuat Matriks Perbandingan Berpasangan

Prioritas pengguna:

1. Harga → paling penting  
2. Keunikan & Berat → penting  
3. Memori, Warna, Kamera → prioritas terakhir  

Matriks perbandingan kriteria:

| Kriteria | H | M | W | K | B | U |
|---|---|---|---|---|---|---|
| Harga | 1 | 5 | 5 | 5 | 3 | 3 |
| Memori | 1/5 | 1 | 1 | 1 | 1/3 | 1/3 |
| Warna | 1/5 | 1 | 1 | 1 | 1/3 | 1/3 |
| Kamera | 1/5 | 1 | 1 | 1 | 1/3 | 1/3 |
| Berat | 1/3 | 3 | 3 | 3 | 1 | 1 |
| Unik | 1/3 | 3 | 3 | 3 | 1 | 1 |

---

# Tahap 4 — Normalisasi Matriks

Rumus normalisasi:

```math
w_j = \frac{a_{ij}}{\sum a_{ij}}
```

Hasil normalisasi:

| Kriteria | Bobot |
|---|---|
| Harga | 0.4188 |
| Memori | 0.0689 |
| Warna | 0.0689 |
| Kamera | 0.0689 |
| Berat | 0.1872 |
| Keunikan | 0.1872 |

---

# Tahap 5 — Menghitung Nilai Bobot Kriteria

```text
W = (
0.4188,
0.0689,
0.0689,
0.0689,
0.1872,
0.1872
)
```

Artinya:
- Harga menjadi faktor paling dominan.
- Berat dan Keunikan berada di prioritas kedua.

---

# Tahap 6 — Mengukur Consistency Index (CI)

Rumus:

```math
CI = \frac{\lambda_{max}-n}{n-1}
```

Diperoleh:

- λmax = 6.0579
- n = 6

Perhitungan:

```text
CI = (6.0579 - 6) / (6 - 1)
CI = 0.0116
```

---

# Tahap 7 — Menghitung Consistency Ratio (CR)

Rumus:

```math
CR = \frac{CI}{RI}
```

Untuk n = 6:
- RI = 1.24

Perhitungan:

```text
CR = 0.0116 / 1.24
CR = 0.0093
```

Karena:

```text
CR ≤ 0.1
```

Maka matriks dinyatakan konsisten.

---

# Tahap 8 — Uji Konsistensi Hierarki

Karena nilai CR memenuhi syarat konsistensi, maka proses dapat dilanjutkan ke tahap berikutnya.

---

# Data Alternatif HP

| HP | Harga | Memori | Warna | Kamera | Berat |
|---|---|---|---|---|---|
| N70 | 2.3 jt | 35 MB | 256 KB | 2 MP | 126 gr |
| N73 | 3.1 jt | 42 MB | 256 KB | 3.2 MP | 116 gr |
| N80 | 3.7 jt | 40 MB | 256 KB | 3.2 MP | 134 gr |
| N90 | 4.7 jt | 90 MB | 16 MB | 2 MP | 191 gr |

---

# Tahap 9 — Membuat Matriks Perbandingan Alternatif

Dilakukan untuk setiap kriteria:
- Harga
- Memori
- Warna
- Kamera
- Berat
- Keunikan

Contoh hasil bobot alternatif:

| Alternatif | Harga | Memori | Warna | Kamera | Berat | Keunikan |
|---|---|---|---|---|---|---|
| N70 | 0.3505 | 0.1691 | 0.0149 | 0.1932 | 0.2713 | 0.0860 |
| N73 | 0.2601 | 0.2029 | 0.0149 | 0.3077 | 0.2947 | 0.1544 |
| N80 | 0.2179 | 0.1932 | 0.0149 | 0.3077 | 0.2551 | 0.2415 |
| N90 | 0.1715 | 0.4348 | 0.9552 | 0.1932 | 0.1790 | 0.5181 |

---

# Tahap 10 — Normalisasi Matriks Alternatif

Setiap matriks alternatif dinormalisasi dan dihitung rata-rata bobot prioritasnya.

---

# Tahap 11 — Perkalian Bobot Kriteria dan Alternatif

Rumus:

```math
s_j = \sum_i (s_{ij})(w_i)
```

Hasil akhir:

| Alternatif | Nilai Akhir |
|---|---|
| N70 | 0.2396 |
| N73 | 0.2292 |
| N80 | 0.2198 |
| N90 | 0.3114 |

---

# Tahap 12 — Perangkingan

| Ranking | HP | Nilai |
|---|---|---|
| 1 | N90 | 0.3114 |
| 2 | N70 | 0.2396 |
| 3 | N73 | 0.2292 |
| 4 | N80 | 0.2198 |

---

# Kesimpulan

Berdasarkan metode AHP:

> HP yang direkomendasikan untuk dibeli adalah **N90** karena memiliki nilai prioritas tertinggi yaitu **0.3114**.

Hal ini menunjukkan bahwa N90 paling sesuai dengan kebutuhan pengguna berdasarkan kombinasi:
- memori besar,
- warna lebih banyak,
- bentuk unik,
- serta bobot prioritas kriteria yang telah ditentukan.

---

# Coding Python Metode AHP

```python
import numpy as np

# Bobot kriteria
bobot_kriteria = np.array([
    0.4188,
    0.0689,
    0.0689,
    0.0689,
    0.1872,
    0.1872
])

# Bobot alternatif
alternatif = np.array([
    [0.3505, 0.1691, 0.0149, 0.1932, 0.2713, 0.0860],
    [0.2601, 0.2029, 0.0149, 0.3077, 0.2947, 0.1544],
    [0.2179, 0.1932, 0.0149, 0.3077, 0.2551, 0.2415],
    [0.1715, 0.4348, 0.9552, 0.1932, 0.1790, 0.5181]
])

# Nama alternatif
nama_hp = ["N70", "N73", "N80", "N90"]

# Perhitungan skor akhir
hasil = alternatif.dot(bobot_kriteria)

# Menampilkan hasil
for i in range(len(nama_hp)):
    print(nama_hp[i], "=", round(hasil[i], 4))

# Ranking
ranking = sorted(
    zip(nama_hp, hasil),
    key=lambda x: x[1],
    reverse=True
)

print("\\nRanking HP:")
for i, (nama, skor) in enumerate(ranking, start=1):
    print(i, nama, "=", round(skor, 4))
```
