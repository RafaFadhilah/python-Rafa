print("=== BELANJA ===")
print("1 = Member")
print("2 = Non Member")

pelanggan = int(input("Masukkan Jenis pelanggan (1 atau 2) : "))
belanja = float(input("Masukkan total belanja : "))

match pelanggan:
    case 1:
        if belanja >= 100.000:
            print("Diskon = 10%")
        else:
            print("Diskon = 0%")
    case 2:
        if belanja >= 100.000:
            print("Diskon = 5%")
        else:
            print("Diskon = 0%")
    case _:
        print("jenis pelanggan tidak valid.")