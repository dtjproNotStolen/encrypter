from random import randint
from scripst import *

loadNewKey = True



input1 = "hi"

string_Array = []

for i in input1:
    string_Array.append(i)

lenght = len(string_Array)




print(string_Array)
print(lenght)

#hasher
if loadNewKey:
    key = Encrypter.gen_key(lenght)
else:
    key = [2,2]
for i in range(lenght):
    string_Array[i] = Encrypter.char_to_int(string_Array[i])
    string_Array[i] = Encrypter.change_char_pos(key[i], string_Array[i])
    string_Array[i] = Encrypter.int_to_char(string_Array[i])
print(key)
print(string_Array)

for i in range(lenght):
    string_Array[i] = Decrypter.char_to_int(string_Array[i])
    string_Array[i] = Decrypter.change_char_pos(key[i], string_Array[i])
    string_Array[i] = Decrypter.int_to_char(string_Array[i])
print(string_Array)