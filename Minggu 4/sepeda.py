class Sepeda:
    """
    Implementasi kelas sepeda. 
    NOTE: Jangan ubah konstruktor dan nama fungsi beserta jumlah argumen-nya
    """
    def __init__(self):
        self.roda_gigi_saat_ini = 1
        self.max_kecepatan = 2
        self.kecepatan = 0
        
    def pindah_roda_gigi(self, roda_gigi):
        """
        berpindah gigi sesuai paramter roda_gigi
        """
        if roda_gigi < 5:
            self.roda_gigi_saat_ini = roda_gigi
            self.max_kecepatan =roda_gigi * 2
            print("Roda gigi sepeda sekarang: ", self.roda_gigi_saat_ini)
            print ("Max kecepatan", self.max_kecepatan)
        pass
    
    def tambah_kecepatan(self):
        """
        kecepatan bertambah 1
        """
        if self.kecepatan < self.max_kecepatan:
            self.kecepatan += 1
            print("Kecepatan sepeda sekarang: ", self.kecepatan)
        pass
        
    def kurang_kecepatan(self):
        """
        kecepatan berkurang 1
        """
        if self.kecepatan > 0:
            self.kecepatan -= 1
            print("Kecepatan sepeda sekarang: ", self.kecepatan)
        pass
