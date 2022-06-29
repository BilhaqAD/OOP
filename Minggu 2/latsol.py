numbers = [12, 37, 5, 42, 8, 3]
print(numbers)
satudigit = []
duadigit = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number > 9):
        duadigit.append(number)
    else:
        satudigit.append(number)
print("======")
print(numbers)
print("Ini Satuan", satudigit)
print("Ini Puluhan", duadigit)