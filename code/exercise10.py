# Խնդիր 10: Սահմանել ֆունկցիա, որը վերադարձնում է տրված 
#           n թվի թվանշանների քանակը։

def digits(n):
    count = 0
    while n != 0:
        n = int(n / 10)
        count += 1
    return count


print(digits(0))
print(digits(10))
print(digits(999))

