from abc import ABC, abstractclassmethod

class Kendaraan(ABC):
    @abstractclassmethod
    def get_maju(self):
        pass

    @abstractclassmethod
    def get_berhenti(self):
        pass

    @abstractclassmethod
    def get_ngebut(self):
        pass

class Mobil(Kendaraan):
    def __init__(self, warna, harga):
        self.warna = warna
        self.harga = harga # dalam juta
    def get_maju(self):
        print("Mobil maju")

    def get_berhenti(self):
        print("Mobil berhenti")

    def get_ngebut(self):
        print("Mobil ngebut")

    def klakson(self):
        print("Beep Beep!")

class Motor(Kendaraan):
    def __init__(self, warna, harga):
        self.warna = warna
        self.harga = harga # dalam juta

    def get_maju(self):
        print("Motor maju")

    def get_berhenti(self):
        print("Motor berhenti")

    def get_ngebut(self):
        print("Motor ngebut")

    def klakson(self):
        print("Beep Beep!")

class Truk(Kendaraan):
    def __init__(self, warna, harga):
        self.warna = warna
        self.harga = harga # dalam juta

    def get_maju(self):
        print("Truk maju")

    def get_berhenti(self):
        print("Truk berhenti")

    def get_ngebut(self):
        print("Truk ngebut")

    def klakson(self):
        print("Beep Beep!")

mobil1 = Mobil("Hitam", 120)
mobil1.get_maju()
mobil1.klakson()

motor1 = Motor("Merah", 20)
motor1.get_ngebut()

Truk1 = Truk("Biru", 400)
Truk1.get_berhenti()

    