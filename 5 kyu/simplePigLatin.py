import string

def pig_it(text):
    text = text.split()
    conv_str = ""
    for idx, word in enumerate(text):
        if len(word) >= 2 or word in string.ascii_letters:
            conv_str += word[1:]+word[0] + 'ay '
        else:
            conv_str += word
    return conv_str[0:-1]


print(pig_it('adsahwsf hfdgf jhetg ! dsad'))