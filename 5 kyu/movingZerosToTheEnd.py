def move_zeros(array):
    # zero_arr = [0 for num in array if num == 0]
    # array = [num for num in array if num != 0]
    # return array + zero_arr
    return [num for num in array if num != 0] + [0 for num in array if num == 0]

zeros = [9, 0, 0, 2, 3, 0, 1, 0 , 0, 4, 0]



print(move_zeros(zeros))