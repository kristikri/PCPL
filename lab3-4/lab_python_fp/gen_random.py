import random

def gen_random(count, minim, maxim):
    for _ in range(count):
        yield random.randint(minim, maxim)

for num in gen_random(5, 1, 3):
    print(num)