print("=== KATEGORI UJIAN ===")
print("1 = Teori")
print("2 = Praktik")

kategori = int(input("Masukkan kategori ujian : "))
nilai = int(input("Masukkan Nilai Ujian : "))

match kategori:
    case 1:
        if nilai >= 75:
            print("Selamat, anda lulus")
        else:
            print("Maaf, anda belum lulus")
    case 2:
        if nilai >= 75:
            print("Selamat, anda lulus")
        else:
            print("Maaf, anda belum lulus")
    case _:
        print("Kategori ujian tidak valid.")