numbers = [5, 3, 1, 8, 0]
def sort_array(source_array):
    odds = iter(sorted([num for num in numbers if num % 2 != 0]))
    return [next(odds) if num % 2 != 0 else num for num in numbers]


print(sort_array(numbers))