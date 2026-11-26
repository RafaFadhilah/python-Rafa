print("=== NAMA BULAN ===")
print("1.Januari")
print("2.Februari")
print("3.Maret")
print("4.April")
print("5.Mei")
print("6.Juni")

bulan = int(input("Masukkan No Bulan (1-6): "))
match bulan:
    case 1:
        print("Januari")
    case 2:
        print("Februari")
    case 3:
        print("Maret")
    case 4:
        print("april")
    case 5:
        print("Mei")
    case 6:
        print("Juni")
    case _:
        print("Bulan tidak tersedia.")