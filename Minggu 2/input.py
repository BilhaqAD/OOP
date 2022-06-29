nama = input("Nama kamu: ")
print("Halo, " + nama + "!")

passw = input("Password: ")
real_pass = "baka123"

while passw != real_pass:
    print("Password salah!")
    passw = input("Password: ")

print("Password benar!, Login berhasil!")

for i in range(10):
    if i % 2 != 0:
        print(i)