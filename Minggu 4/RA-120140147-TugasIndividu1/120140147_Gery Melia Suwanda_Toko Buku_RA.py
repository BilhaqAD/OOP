#Nama : Gery Melia Suwanda
#NIM  : 120140147
#kelas: RA

class TokoBuku :
    def __init__(self, nama, alamat, telepon, buku):
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.buku = buku

    def cetakData(self) :
        print("Nama     :", self.nama)
        print("Alamat   :", self.alamat)
        print("Telepon  :", self.telepon)
        print("Buku yang tersedia :")
        for i in self.buku :
            print("\t", i)

    def tambahBuku(self):
        buku=input("Masukkan judul buku : ")
        self.buku.append(buku)
    def hapusBuku(self) :
        buku=input("Masukkan judul buku : ")
        self.buku.remove(buku)
    def cetakSemuaBuku(self) :
        print("Buku yang tersedia :")
        for i in self.buku :
            print("\t", i)
    def cetakJumlahBuku(self) :
        print("Jumlah buku :", len(self.buku))

TokoGery=TokoBuku("Toko Gery","Jl. Kebon Jeruk No.1", "08123456789", ["Buku Tulis", "Buku Komputer", "Buku Alat Tulis"])
TokoGery.cetakData()
print("Ingin menambah buku? (y/n)")
if input() == "y" :
    TokoGery.tambahBuku()
    TokoGery.cetakSemuaBuku()
else :
    TokoGery.cetakJumlahBuku()
print("Ingin menghapus buku? (y/n)")
if input() == "y" :
    TokoGery.hapusBuku()
    TokoGery.cetakSemuaBuku()
else :
    TokoGery.cetakJumlahBuku()