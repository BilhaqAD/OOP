class MyError(Exception):
    def __str__(self):
        return "Terjadi MyError"


def some_function(a, b):
    assert isinstance(a, str), "parameter a harus string"
    assert isinstance(b, int), "parameter b harus bilangan bulat"
    if int(b) < 0:
        raise MyError(
            "Tidak dapat duplikasi string karena parameter bernilai negatif")
    return a * b


#a = "str"
#b = 5

a = "hai"
b = -2

#print(some_function(a, b))

#try:
#  print(some_function(a, b))
#except MyError as e:
#  print(some_function(a, -b))
#finally:
#  print("Finally executed")

PATH = "main.py"

f = None
try:
  f = open(PATH, 'r') # resource nya di-lock
except FileNotFoundError:
  print("File not found")
finally:
  f.close() # release lock
