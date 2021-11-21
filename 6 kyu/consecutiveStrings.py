alpha = ["maxim", "vikaa", "kol", "dog", "player"]

def longest_consec(strarr, k):
    vars = []
    current = k
    start_v = 0
    if len(strarr) < k:
        return ""
    else:
        while True:
            value = ""
            for i in range(start_v, current):
                value += strarr[i]
            vars.append(value)
            current += 1
            start_v += 1
            if current > len(strarr):
                word = ""
                for w in vars:
                    if len(w) > len(word):
                        word = w
                return word

print(longest_consec(alpha, 4))