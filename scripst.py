from random import randint

charss = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']

class Encrypter:


    def int_to_char(inp):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
        return chars[inp]


    def char_to_int(inp):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
        for i in range(len(chars)):
            if inp == chars[i]:
                return i

    def change_char_pos(inval, intput):
        temp = intput + inval
        if temp >= 25:
            temp -= 25
        return temp

    def gen_key(lenght):
        lenght += 0
        hashKey = []
        for i in range(lenght):
            hashKey.append(randint(0,24))
        return hashKey



class Decrypter:


    def int_to_char(inp):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
        return chars[inp]


    def char_to_int(inp):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
        for i in range(len(chars)):
            if inp == chars[i]:
                return i

    def change_char_pos(inval, intput):
        temp = intput - inval
        if temp <= -1:
            temp += 25
        return temp
    
