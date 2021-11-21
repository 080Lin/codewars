import string

def is_pangram(s):
    for i in string.ascii_lowercase:
        if not i in s.lower():
            return False
    return True

is_pangram('dasdGDSAGEFsdv')