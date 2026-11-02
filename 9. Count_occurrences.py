def count_occurrences(items, target):
    '''count occurrences of a target in item'''
    target_times = 0

    for i in items:
        if i == target:
            target_times = target_times + 1

    return target_times

print(count_occurrences(["a", "b", "a"], "a"))
