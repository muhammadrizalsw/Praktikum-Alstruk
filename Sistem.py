while True:
    print("\n=== SISTEM LAYANAN TATA USAHA (TU) ===")
    print("1. Peminjaman Proyektor")
    print("2. Layanan Berkas Absensi Manual")
    print("3. Peminjaman Alat Lain (Kabel Roll / Spidol)")
    print("0. Keluar dari Aplikasi")

    pilihan = input("\nPilih jenis layanan (0-3): ").strip()

    if pilihan == "1":
        print("\n--- Layanan Peminjaman Proyektor ---")
        membawa_ktm = input("Apakah membawa Kartu Tanda Mahasiswa (KTM)? (y/n): ").strip().lower()
        ada_jadwal = input("Apakah ada jadwal perkuliahan hari ini? (y/n): ").strip().lower()
        
        if membawa_ktm == 'y' and ada_jadwal == 'y':
            print("\nSTATUS: APPROVED")
            print("-> Proyektor diserahkan. Silakan tinggalkan KTM di loket TU sebagai jaminan.")
            print("-> Wajib dikembalikan maksimal 15 menit setelah jam kuliah selesai.")
        elif membawa_ktm == 'y' and ada_jadwal == 'n':
            print("\nSTATUS: REJECTED")
            print("-> Peminjaman proyektor hanya diizinkan sesuai jadwal kuliah aktif.")
        else:
            print("\nSTATUS: REJECTED")
            print("-> Peminjaman ditolak karena tidak membawa KTM fisik sebagai jaminan.")

    elif pilihan == "2":
        print("\n--- Layanan Berkas Absensi Manual ---")
        status_absensi = input("Pilih aksi (1: Ambil Absensi / 2: Kembalikan Absensi): ").strip()
        
        if status_absensi == "1":
            nama_matkul = input("Masukkan Nama Mata Kuliah: ")
            nama_dosen = input("Masukkan Nama Dosen Pengampu: ")
            print(f"\nSTATUS: BERKAS DISERAHKAN")
            print(f"-> Berkas absensi fisik '{nama_matkul}' (Dosen: {nama_dosen}) berhasil diambil.")
        elif status_absensi == "2":
            print("\nSTATUS: BERKAS DITERIMA")
            print("-> Berkas absensi fisik telah dikembalikan dan dicatat oleh petugas TU.")
        else:
            print("\nSTATUS: ERROR - Pilihan aksi tidak valid.")

    elif pilihan == "3":
        print("\n--- Layanan Peminjaman Alat Tambahan ---")
        nama_barang = input("Masukkan nama barang (contoh: Kabel Roll / Spidol): ")
        print(f"\nSTATUS: DIPROSES - Petugas sedang memeriksa ketersediaan {nama_barang} di gudang.")

    elif pilihan == "0":
        print("\nTerima kasih telah menggunakan sistem layanan TU.")
        break

    else:
        print("\nSTATUS: ERROR - Pilihan menu tidak valid.")

    kembali = input("\nApakah ingin kembali ke menu utama? (y/n): ").strip().lower()
    if kembali != 'y':
        print("\nTerima kasih telah menggunakan sistem layanan TU.")
        break
