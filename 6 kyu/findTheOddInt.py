a = [1, 1, 2]
b = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
c = [10]

def find_it(seq):
    seqv = {}
    for value in seq:
        if value in seqv:
            seqv[value] += 1
        else:
            seqv[value] = 1

    return list({k: v  for k, v in seqv.items() if v % 2 != 0}.keys())[0]


find_it(b)
