# Խնդիր 3։ Գրել ծրագիր, որը պահանջում է ներմուծել 
#          երեք թիվ և արտածում է դրանցից ամենափոքրը։

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

small = a

if b < small:
    small = b

if c < small:
    small = c

print('The smallest of', a, b, c, 'is', small)

