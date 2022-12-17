
def search(value, elements):
    for el in elements:
        if el == value:
            return True
    return False


months = ['հունվար', 'փետրվար', 'մարտ', 'ապրիլ', 'մայիս', 'հունիս']
result = search('հունվար', months)
print(result)

result = search('դեկտեմբեր', months)
print(result)
