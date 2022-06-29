PATH = "main.py" # path file location

f = open(PATH, "r") # buka file dengan mode read
print(len(f.read())) # print panjang file

class MyError(Exception):
    pass

def baca_file(PATH):
    # buat variabel file
    f = open(PATH, 'r')
    # buat variabel baris
    size = len(f.readlines())
    if size > 1024:
        f.seek(0)
        print(len(f.read()))
        raise MyError("“File terlalu besar, maksimal adalah 1024 Byte, file Anda berukuran:")

    f.seek(0) # pindah ke baris pertama
    return

if __name__ == "__main__":
    f = None
    try:
        f = baca_file(PATH)
        print("File berhasil dibaca")
    except FileNotFoundError:
        print("Tidak ada file tersebut")
    except MyError:
        print("My Error")
    finally:
        if f is not None:
            f.close()
    