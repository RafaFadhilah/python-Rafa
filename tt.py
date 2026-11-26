
print("==== FILM BIOSKOP ====")

usia = int(input("Masukkan usia : "))

if usia >= 17:
    print("\nPilih Genre Film:")
    print("1. Horor")
    print("2. Komedi")
    print("3. Keluarga")
    print("4. Aksi")

    genre = int(input("Masukkan pilihan genre (1-4): "))

    if genre == 1:
        print("\nPilihan Film Horor:")
        print("1. Horor Indonesia")
        print("2. Horor Luar Negeri")
        pilihan = int(input("Pilih film (1-2): "))

        if pilihan == 1:
            judul = "Horor Indonesia"
        elif pilihan == 2:
            judul = "Horor Luar Negeri"
        else:
            judul = "Pilihan tidak valid"

    elif genre == 2:
        print("\nPilihan Film Komedi:")
        print("1. Komedi Indonesia")
        print("2. Komedi Luar Negeri")
        pilihan = int(input("Pilih film (1-2): "))

        if pilihan == 1:
            judul = "Komedi Indonesia"
        elif pilihan == 2:
            judul = "Komedi Luar Negeri"
        else:
            judul = "Pilihan tidak valid"

    elif genre == 3:
        print("\nPilihan Film Keluarga:")
        print("1. Keluarga Indonesia")
        print("2. Keluarga Luar Negeri")
        pilihan = int(input("Pilih film (1-2): "))

        if pilihan == 1:
            judul = "Keluarga Indonesia"
        elif pilihan == 2:
            judul = "Keluarga Luar Negeri"
        else:
            judul = "Pilihan tidak valid"

    elif genre == 4:
        print("\nPilihan Film Aksi:")
        print("1. Hollywood")
        print("2. Indonesia")
        print("3. Bollywood")
        pilihan = int(input("Pilih film (1-3): "))

        if pilihan == 1:
            judul = "Film Aksi Hollywood"
        elif pilihan == 2:
            judul = "Film Aksi Indonesia"
        elif pilihan == 3:
            judul = "Film Aksi Bollywood"
        else:
            judul = "Pilihan tidak valid"

    else:
        judul = "Pilihan tidak valid"

else:
    print("\nPilih Jenis Film Animasi:")
    print("1. Animasi 2D")
    print("2. Animasi 3D")

    animasi = int(input("Masukkan pilihan (1-2): "))

    if animasi == 1:
        print("\nPilihan Film Animasi 2D:")
        print("1. Naruto")
        print("2. One Piece")
        pilihan = int(input("Pilih film (1-2): "))

        if pilihan == 1:
            judul = "Naruto"
        elif pilihan == 2:
            judul = "One Piece"
        else:
            judul = "Pilihan tidak valid"

    elif animasi == 2:
        print("\nPilihan Film Animasi 3D:")
        print("1. Nemo")
        print("2. Kungfu Panda")
        pilihan = int(input("Pilih film (1-2): "))

        if pilihan == 1:
            judul = "Nemo"
        elif pilihan == 2:
            judul = "Kungfu Panda"
        else:
            judul = "Pilihan tidak valid"

    else:
        judul = "Pilihan tidak valid"

if judul == "Pilihan tidak valid":
    print("\nMaaf, pilihan Anda tidak valid.")
else:
    print('\nSelamat Menyaksikan "' + judul + '"')
