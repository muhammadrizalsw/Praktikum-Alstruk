nama = input("Masukkan nama mahasiswa: ")

tugas, uts, uas = map(
    float, input("Masukkan nilai Tugas, UTS, UAS: ").split(",")
)

nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
status = "Lulus" if nilai_akhir >= 60 else "Belum Lulus"

print(f"\nNama: {nama}\nNilai Akhir: {nilai_akhir:.2f}\nStatus: {status}")
