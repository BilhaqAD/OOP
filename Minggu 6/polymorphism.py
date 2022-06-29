class Angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek):
        return Angka(self.angka + objek.angka)

    def __str__(self):
        return f"Objek Angka dengan nilai {self.angka}"

x1 = Angka(30)
x2 = Angka(50)

print(x1)
print(x2)
print(x1 + x2)