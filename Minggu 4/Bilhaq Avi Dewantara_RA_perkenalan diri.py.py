class Home: 
  # Constructor
  def __init__(self, warna, alamat):
    self.warna = warna
    self.alamat = alamat

class Person: # Berukut merupakan definisi class Person yang berfungsi untuk menampung data diri pada saat pembuatan objek
  # Constructor
  def __init__(self, nama, usia, asal, prodi, rumah, kampus):
    self.nama = nama
    self.usia = usia
    self.asal = asal
    self.prodi = prodi
    self.rumah = rumah
    self.kampus = kampus
  # Method
  def perkenalan(self): # Berukut merupakan definisi method perkenalan yang berfungsi untuk menampilkan data diri ke layar
    print("Assalamualaikum Warahmatullahi Wabarakatuh,\n")
    print("Halo semuanya :)")
    print(f"Perkenalkan saya {self.nama} berusia {self.usia}.")
    print(f'Saya memiliki rumah bewarna {self.rumah.warna} di {self.asal} dengan alamat {self.rumah.alamat}.')
    print(f"Saat ini saya sedang menempuh pendidikan S1 {self.prodi} di {self.kampus}. Terimakasih.")
    print()
    print("Cheers!,\n")
    print(self.nama)
# Object
data = Person(
    nama = "Bilhaq Avi Dewantara",
    usia = "19",
    asal = "Depok, Jawa Barat, Indonesia",
    prodi= "Teknik Informatika",
    rumah = Home(
        warna = "Abu-abu",
        alamat = "Jl. Raya Bogor Km. 37"
    ),
    kampus = "Institut Teknologi Sumatera"
)

data.perkenalan() # Berukut merupakan pemanggilan method perkenalan yang berfungsi untuk menampilkan data diri ke layar