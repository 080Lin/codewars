def first_non_repeating_letter(string):
    if string == '':
        return ''
    for i in [x for x in string if string.count(x) == 1]:
        if i.lower() != i and i.lower() in string:
            pass
        elif i.upper() != i and i.upper() in string:
            pass
        else:
            return i
    return ''
        
strin = 'sTreSS'

print(first_non_repeating_letter(strin))