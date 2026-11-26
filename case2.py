print("=== MENU MINUMAN ===")
print("1.Es Teh")
print("2.Es Jeruk")
print("3.Kopi")
print("4.Susu")

menu = int(input("Masukkan No Minuman(1-4): "))
match menu:
    case 1:
        print("ES TEH\NHARGA Rp5.000")
    case 2:
        print("ES JERUK\NHARGA Rp7.000")
    case 3:
        print("KOPI\NHARGA Rp8.000")
    case 4:
        print("SUSU\NHARGA Rp6.000")
    case _:
        print("Menu tidak tersedia.")