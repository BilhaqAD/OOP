import abc

class Pegawai(abc.ABC):
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    @abc.abstractmethod
    def hitung_gaji(self):
        print("Hitung gaji")

class Manager(Pegawai):
    def hitung_gaji(self):
        print("Hitung gaji manager")

peg = Pegawai("Adam", "12345")
print(peg.nama)