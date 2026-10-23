def jalankan_rekap(nama, nilai_tugas, nilai_ujian):
    rata_rata = (nilai_tugas + nilai_ujian) / 2

    status_lulus = rata_rata >= 75

    print("=== REKAP NILAI MAHASISWA ===")
    print("Nama Mahasiswa :", nama)
    print("Nilai Tugas    :", nilai_tugas)
    print("Nilai Ujian    :", nilai_ujian)
    print("Rata-Rata      :", rata_rata)
    print("Status Lulus   :", status_lulus)
    print("-----------------------------\n")

jalankan_rekap("Alya", 80, 85)

jalankan_rekap("Rizal", 60, 70)