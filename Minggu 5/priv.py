class Sepeda:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna  
        self.__max_speed = 2
        

    def get_kecepatan(self):
        return self.__kecepatan

    def get_max_kecepatan(self):
        return self.__max_kecepatan

sepedaku = Sepeda()
sepedaku.__max_kecepatan = 11
print(sepedaku.get_max_kecepatan())
print(sepedaku.__max_kecepatan)