class Ayah:
    def __init__ (self, nama, jk):
        self.nama = nama
        self.jk = jk

    def bertani(self):
        teks = "{} bertani di sawah"

        return teks.format(self.nama)

class Ibu:
    def __init__(self, nama, jk):
        self.nama = nama
        self.jk = jk

    def memasak(self):
        teks = "{} memasak di dapur"

        return teks.format(self.nama)

class Anak(Ayah, Ibu):
    def __init__(self, nama, jk):
        super().__init__(nama, jk)

anak1 = Anak("Mustafa", "Pria")


print(anak1.bertani())
print(anak1.memasak())