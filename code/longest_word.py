

def longest_word(text):
    words = text.split(' ')

    cur_woord = words[0]
    length = len(cw)

    for w in words:
        l = len(w)
        if length < l:
            length = l
            cur_woord = w
    
    return cur_woord

