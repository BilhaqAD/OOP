# Class Playlist
class Playlist:
    """
    Playlist memiliki atribut
     - daftar_lagu = sebuah list yang berisi daftar objek Lagu
     - track_saat_ini = penanda indeks lagu saat ini
    """
    
    # Definisi konstruktor: 
    # Saat playlist baru dibuat, playlist kosong 
    # daftar_lagu = None dan track_saat_ini = None
    def __init__(self):
        self.daftar_lagu = None
        self.track_saat_ini = None
    
    # Fungsi tambah lagu:
    # Menambahkan satu objek lagu pada akhir list daftar_lagu
    # ARGUMEN: `new_lagu` merupakan sebuah objek lagu yang akan ditambahkan
    def tambah_lagu(self, new_lagu):
        if self.daftar_lagu is None:
            self.daftar_lagu = [new_lagu]
            self.track_saat_ini = 0
        else:
            self.daftar_lagu.append(new_lagu)
    
    # Fungsi private set lagu:
    # Set lagu yang akan diputar dan mainkan lagu tersebut. Kondisi yang mungkin:
    # - Jika playlist kosong, lagu tidak dapat diputar. Anda harus mencetak: "GAGAL MEMUTAR LAGU: PLAYLIST KOSONG"
    # - Jika lagu saat ini merupakan lagu pertama, lagu sebelumnya adalah lagu terakhir
    # - Setelah memutar lagu terakhir, lagu selanjutnya kembali ke lagu pertama
    # Pada bagian akhir fungsi ini, anda hanya perlu mencetak informasi lagu yang diputar saat ini dengan memanggil fungsi now_playing 
    # ARGUMEN: `track` merupakan nomor indeks lagu dalam playlist
    def __set_and_play(self, track):
        # implementasi
        if self.daftar_lagu is None:
            track = None
        else:
            self.track_saat_ini = track
            track = self.daftar_lagu[self.track_saat_ini]
        # akhir pemanggilan fungsi, berikan parameter yang sesuai
        Playlist.now_playing(track)
    
    # Fungsi putar lagu pertama:
    # Memutar lagu pada indeks pertama dari daftar_lagu
    def play_first(self):
        # contoh implementasi
        self.__set_and_play(0)
    
    # Fungsi putar lagu terakhir:
    # Memutar lagu pada indeks terakhir dari daftar_lagu
    def play_last(self):
        # implementasi
        self.__set_and_play(-1)
        
    # Fungsi putar lagu:
    # Memutar lagu sesuai indeks yang ditujuk oleh track_saat_ini
    def play(self):
        # implementasi
        self.__set_and_play(self.track_saat_ini)
    
    # Fungsi putar lagu selanjutnya:
    # Memutar lagu selanjutnya
    def play_next(self):
        # implementasi
        if self.track_saat_ini == len(self.daftar_lagu) - 1:
            self.track_saat_ini = 0
        else:
            self.track_saat_ini +=1
            
        self.__set_and_play(self.track_saat_ini)
    
    # Fungsi putar lagu sebelumnya:
    # Memutar lagu selanjutnya
    def play_previous(self):
        # implementasi
        self.track_saat_ini -= 1
        self.__set_and_play(self.track_saat_ini)

    # JANGAN UBAH FUNGSI INI
    # Fungsi static menampilkan informasi lagu yang sedang diputar
    # ARGUMEN: `lagu` merupakan sebuah objek dari kelas Lagu 
    @staticmethod
    def now_playing(lagu):
        if lagu is None:
            print("<b>GAGAL MEMUTAR LAGU</b>: PLAYLIST KOSONG")
        else:
            print("Memutar lagu <b>{:s}</b> by <b>{:s}<b>".format(lagu.judul_lagu, lagu.artis))