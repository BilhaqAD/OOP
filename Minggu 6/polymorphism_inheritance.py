class Hewan:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def bersuara (self):
        pass

class Kucing(Hewan):
    def bersuara (self):
        return "Meow"

class Anjing(Hewan):
    def bersuara (self):
        return "Guk Guk"
        
kucing = Kucing("Tom", 3)
anjing = Anjing("Jerry", 2)

for hewan in (kucing, anjing):
    print(hewan.bersuara())