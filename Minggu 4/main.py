class table :
    def __init__(self, jenis_meja, tinggi, panjang, lebar, warna, bahan):
        self.jenis_meja = jenis_meja
        self.tinggi = tinggi
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna
        self.bahan = bahan

    def cetak_meja(self):
        print("Tinggi meja :", self.tinggi)
        print("Lebar meja  :", self.lebar)
        print("Panjang meja :", self.panjang)
        print("Warna meja   :", self.warna)
        print("Bahan meja   :", self.bahan)
        print("Jenis meja   :", self.jenis_meja)
        print("\n")
    
class TableShop:

    def __init__(self, nama, alamat, telepon, meja):
        self.nama = nama
        self.alamat = alamat
        self.telepon = telepon
        self.meja = meja
        
    
    def cetak_info(self):
        print("Nama    :", self.nama)
        print("Alamat  :", self.alamat)
        print("Telepon :", self.telepon)
        print("\n---DATA MEJA---")
        h=0
        for i in self.meja :
            h+=1
            print("Meja ke-"+ str(h))
            i.cetak_meja()


majaMakan = table("meja makan", "1.5 meter", "2 meter", "2 meter", "merah", "kayu jati")
majaBelajar = table("meja belajar", "1.5 meter", "2 meter", "0.8 meter", "coklat", "kayu jati")
majaTamu = table("meja tamu", "75 cm", "50 cm", "120 cm", "Coklat", "Kayu")
majaTidur = table("meja tidur", "75 cm", "50 cm", "120 cm", "Hitam", "Kayu")

TokoMeja = TableShop("Toko Dila", "Jl. Pelita Kebangsaan No. 99", "082387452718", [majaMakan, majaBelajar, majaTamu, majaTidur])
print ()
TokoMeja.cetak_info()