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

key = gen_key(lenght)

for i in range(lenght):
    string_Array[i] = char_to_int(string_Array[i])
    string_Array[i] = change_char_pos(key[i], string_Array[i])
    string_Array[i] = int_to_char(string_Array[i])
print(key)
print(string_Array)