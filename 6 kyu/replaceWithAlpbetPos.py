import string

def alphabet_position(text):
    res = ""
    for i in text.lower():
        if i in string.ascii_lowercase:
            res += (f'{string.ascii_lowercase.index(i) + 1} ')
    return res[:-1]

print(alphabet_position('The narwhal bacons at midnight.'))