import numpy as np

# =========================
# METODE AHP PEMILIHAN HP
# =========================

# -----------------------------------
# 1. Bobot Kriteria
# -----------------------------------
# Harga, Memori, Warna, Kamera, Berat, Keunikan

bobot_kriteria = np.array([
    0.4188,  # Harga
    0.0689,  # Memori
    0.0689,  # Warna
    0.0689,  # Kamera
    0.1872,  # Berat
    0.1872   # Keunikan
])

# -----------------------------------
# 2. Bobot Alternatif
# -----------------------------------
# Baris = Alternatif HP
# Kolom = Kriteria

# Urutan kolom:
# Harga, Memori, Warna, Kamera, Berat, Keunikan

bobot_alternatif = np.array([

    # N70
    [0.3505, 0.1691, 0.0149, 0.1932, 0.2713, 0.0860],

    # N73
    [0.2601, 0.2029, 0.0149, 0.3077, 0.2947, 0.1544],

    # N80
    [0.2179, 0.1932, 0.0149, 0.3077, 0.2551, 0.2415],

    # N90
    [0.1715, 0.4348, 0.9552, 0.1932, 0.1790, 0.5181]

])

# -----------------------------------
# 3. Nama Alternatif
# -----------------------------------

nama_hp = ["N70", "N73", "N80", "N90"]

# -----------------------------------
# 4. Menghitung Nilai Akhir
# -----------------------------------
# Rumus:
# S = bobot alternatif x bobot kriteria

hasil = bobot_alternatif.dot(bobot_kriteria)

# -----------------------------------
# 5. Menampilkan Nilai Akhir
# -----------------------------------

print("=== HASIL PERHITUNGAN AHP ===\n")

for i in range(len(nama_hp)):
    print(f"{nama_hp[i]} = {hasil[i]:.4f}")

# -----------------------------------
# 6. Melakukan Ranking
# -----------------------------------

ranking = sorted(
    zip(nama_hp, hasil),
    key=lambda x: x[1],
    reverse=True
)

print("\n=== HASIL RANKING ===\n")

for i, (nama, skor) in enumerate(ranking, start=1):
    print(f"{i}. {nama} = {skor:.4f}")

# -----------------------------------
# 7. Menentukan HP Terbaik
# -----------------------------------

terbaik = ranking[0]

print("\n=== KESIMPULAN ===")
print(f"HP yang direkomendasikan adalah {terbaik[0]}")
print(f"Dengan nilai akhir sebesar {terbaik[1]:.4f}")