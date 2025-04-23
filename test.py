from random import randint

def gen_key(lenght):
    lenght += 0
    hashKey = []
    for i in range(lenght):
        hashKey.append(randint(0,25))
    return hashKey


print(gen_key(2))