# Խնդիր 8: Սահմանել ֆունկցիա, որը ստանում է չորս թիվ ու 
#          վերադարձնում է դրանցից ամենամեծը։
#          Հուշում. նախ սահմանեք երկու թվերից մեծը որոշող
#          ֆունկցիան, հետո դա օգտագործեք արդեն չորս թվերից
#          ամենամեծը գտնելու համար։

# Երկու թվերից մեծը
def max2(a, b):
    return a if a > b else b

# Չորս թվերից մեծը
def max4(a, b, c, d):
    return max2(max2(a, b), max2(c, d))
