# Խնդիր 4։ Գրել ծրագիր, որը պահանջում է ներմուծել մարդու
#          անուն։ Եթե այդ անունը վերջանում է «ուհի» վերջածանցով,
#          ապա տպում է «Ողջույն տիկին <անուն>», հակառակ 
#          դեպքում «տիկին» բառի փոխարեն տպում է «պարոն»։

name = input('Անունը. ')

if name.endswith('ուհի'):
    print(f'Ողջույն տիկին {name}։')
else:
    print(f'Ողջույն պարոն {name}։')
