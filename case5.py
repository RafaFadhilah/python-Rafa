
print("==== FILM BIOSKOP ====")

usia = int(input("Masukkan usia : "))

if usia >= 17:
    print("\nPilih Genre Film:")
    print("1. Horor")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")

    genre = int(input("Masukkan pilihan genre (1-4): "))

    match genre:
        case 1:
            print("\nPilihan Film Horor:")
            print("1. Alas roban")
            print("2. The conjuring")
            pilihan = int(input("Pilih film (1-2): "))

            match pilihan:
                case 1:
                    judul = "Alas roban"
                case 2:
                    judul = "The conjuring"
                case _:
                    judul = "Pilihan tidak valid"

        case 2:
            print("\nPilihan Film Komedi:")
            print("1. Warkop DKI")
            print("2. MR bean")
            pilihan = int(input("Pilih film (1-2): "))

            match pilihan:
                case 1:
                    judul = "Warkop DKI"
                case 2:
                    judul = "MR Bean"
                case _:
                    judul = "Pilihan tidak valid"

        case 3:
            print("\nPilihan Film Keluarga:")
            print("1. Si Doel")
            print("2. Home alone")
            pilihan = int(input("Pilih film (1-2): "))

            match pilihan:
                case 1:
                    judul = "Si Doel"
                case 2:
                    judul = "Home alone"
                case _:
                    judul = "Pilihan tidak valid"

        case 4:
            print("\nPilihan Film Aksi:")
            print("1. Godzilla minus one")
            print("2. Bima-X")
            print("3. Godzilla Minus zero")
            pilihan = int(input("Pilih film (1-3): "))

            match pilihan:
                case 1:
                    judul = "Godzilla minus one"
                case 2:
                    judul = "Bima-X"
                case 3:
                    judul = "Godzilla Minus zero"
                case _:
                    judul = "Pilihan tidak valid"

        case _:
            judul = "Pilihan tidak valid"

else:
    print("\nPilih Jenis Film Animasi:")
    print("1. Animasi 2D")
    print("2. Animasi 3D")

    animasi = int(input("Masukkan pilihan (1-2): "))

    match animasi:
        case 1:
            print("\nPilihan Film Animasi 2D:")
            print("1. Naruto")
            print("2. One Piece")
            print("3. Tokyo revengers s4")
            pilihan = int(input("Pilih film (1-3): "))

            match pilihan:
                case 1:
                    judul = "Naruto"
                case 2:
                    judul = "One Piece"
                case 3:
                    judul = "Tokyo revengers s4"
                case _:
                    judul = "Pilihan tidak valid"

        case 2:
            print("\nPilihan Film Animasi 3D:")
            print("1. Nemo")
            print("2. Kungfu Panda")
            print("3. Jumbo")
            pilihan = int(input("Pilih film (1-3): "))

            match pilihan:
                case 1:
                    judul = "Nemo"
                case 2:
                    judul = "Kungfu Panda"
                case 3:
                    judul = "Jumbo"
                case _:
                    judul = "Pilihan tidak valid"

        case _:
            judul = "Pilihan tidak valid"

if judul == "Pilihan tidak valid":
    print("\nMaaf, pilihan Anda tidak valid.")
else:
    print("\nSelamat Menyaksikan film", judul)
