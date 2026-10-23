nilai = 82
kehadiran = 90

syarat_nilai = nilai >= 75
syarat_kehadiran = kehadiran >= 80

lulus_and = syarat_nilai and syarat_kehadiran

print("Pemeriksaan Awal (nilai = 82, kehadiran = 90%):")
print("Syarat Nilai (>= 75)     :", syarat_nilai)
print("Syarat Kehadiran (>= 80%):", syarat_kehadiran)
print("Status Kelulusan (and)   :", lulus_and)

nilai = 70
syarat_nilai_baru = nilai >= 75
lulus_and_baru = syarat_nilai_baru and syarat_kehadiran

print("\nSetelah nilai diubah menjadi 70:")
print("Syarat Nilai (>= 75)     :", syarat_nilai_baru)
print("Status Kelulusan (and)   :", lulus_and_baru)

lulus_or_baru = syarat_nilai_baru or syarat_kehadiran
print("Status Kelulusan (or)    :", lulus_or_baru)