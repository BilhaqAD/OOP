# def fungsi_tertentu(a, b, c=7):
#     return a + b + c

# x = fungsi_tertentu(1, 2)
# print(x)

# y = fungsi_tertentu(1, b=2, c=3) # a=1 keyword argument, 2 dan 3 adalah positional argument
# print(y)

# z = fungsi_tertentu(1, b=2, c=3)
# print(z) 

# data = {"nama" : "Andri", "umur" : "20", "hobi" : ["berenang", "makan", "tidur"]}
# print(type(data))       # <class 'dict'>
# print(data['hobi'])     # ['berenang', 'makan', 'tidur']
# print(data['hobi'][1])  # makan
# print(data[0])          # KeyError: 0

# kamus = {'kunci1' : {'sub-kunci1' : 'nilai1'}, 'kunci2' :  { 'sub-kunci2' : 'nilai2'}}
# print(kamus['kunci1'])                  # {'sub-kunci1': 'nilai1'}
# print(kamus['kunci1']['sub-kunci1'])    # nilai1
# print(kamus.items())                    # dict_items([('kunci1', {'sub-kunci1': 'nilai1'}), ('kunci2', {'sub-kunci2': 'nilai2'})])
# print(kamus.values())                   # dict_values([{'sub-kunci1': 'nilai1'}, {'sub-kunci2': 'nilai2'}])

# for i in range(5, 10, 3):
#     print(i)        # 5, 8

kata = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(kata[len(kata)::-1])              # 
print(kata[::-1])                       # 
print(kata[1::2])                       # 


