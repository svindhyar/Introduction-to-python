def find_max(numbers):
    '''Finds max of numbers in a list'''
    max_number = 0

    for score in numbers:
        if max_number < score:
            max_number = score

    return max_number

print(find_max([4, 9, 2]))