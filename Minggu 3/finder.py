##
# A collection of functions to search in lists.
#
##


# Nama fungsi dan argumen jangan diubah
def pemenang_voting(list):
    #Jika list kosong, maka return None
    if len(list) == 0:
        return None
    #Jika list hanya memiliki satu elemen, maka return elemen tersebut
    elif len(list) == 1:
        return list[0]
    #Jika list memiliki lebih dari satu elemen, maka return elemen terbanyak
    else:
        #Inisialisasi dictionary
        dict = {}
        for i in list:
            if i in dict:
                dict[i] +=  1
            else:
                dict[i] = 1
        print(dict)
        #Inisialisasi max dan nama pemenang
        max = 0
        pemenang = ""
        for i in dict:
            if dict[i] > max:
                max = dict[i]
                pemenang = i
        return pemenang
