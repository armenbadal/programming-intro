# Խնդիր 12։ Մոդելավորել նարդու զառը նետելու գործողությունը։ Սահմանել ֆունկցիա, 
#           որ m անգամ նետում է զառը և տպում է, թե որ թիվը քանի անգամ է 
#           հանդիպել։ [Հուշում. Պիթոնն ունի պատահական թվեր գներացնող 
#           random գրադարանը։]

import random

# զառի կողմերի յունիկոդ նիշերը
SIDES = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

def roll_the_dice():
    return SIDES[random.randint(0, 5)]

def simulate_dice_roll(m):
    # կողերի հաշվիչները
    counts = {}

    # քանի դեռ նետումների քանակը զրո չի
    while m > 0:
        # կատարել մեկ նետում
        side = roll_the_dice()
        # պակասեցնել նետման քանակները
        m -= 1
        # փոփոխել հաշվիչը
        counts[side] = counts.get(side, 0) + 1

    # վերադարձնել արդյունքը    
    return counts


# Թեսթեր
print(simulate_dice_roll(6 * 100))
print(simulate_dice_roll(6 * 1000))
print(simulate_dice_roll(6 * 10000))
