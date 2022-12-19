import random

def flip_coin():
    return 'Head' if 1 == random.randint(0, 1) else 'Tail'

def flip_for_heads(n):
    count = 0
    while n > 0:
        count += 1
        if 'Head' == flip_coin():
            n -= 1
    return count

def one_simulation(m):
    count = flip_for_heads(m)
    print(f'{m} «գիր» ստացվել է {count} նետումով։')

one_simulation(10)
one_simulation(100)
one_simulation(1000)
one_simulation(10000)
one_simulation(100000)
