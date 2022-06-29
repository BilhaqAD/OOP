class Koordinat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Koordinat(x, y)

    def __sub__(self, other):
        x = self._x - other.x
        y = self.y - other.y
        return Koordinat(x, y)

    def __str__(self):
        return 'Hasil ({}, {})'.format(self.x, self.y)

titika = Koordinat(1, 5)
titikb = Koordinat(5, 6)
print(titika)
print(titikb)
print(titika + titikb)
