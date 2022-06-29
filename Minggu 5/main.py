##
# Main function of the Python program.
#
##

from playlist import Playlist
from lagu import Lagu

def player():
    player = Playlist()
    song_a = Lagu("Song A", "Artist A")
    player.tambah_lagu(song_a)
    player.play()


if __name__ == '__main__':
    player()
