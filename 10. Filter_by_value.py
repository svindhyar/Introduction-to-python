def filter_by_value(d, minimum):
    '''Filters a dict with minimum number and returns a 
    new dict'''

    d = {"Ana": 15, "Ben": 9}
    minimum = 10

    d2 = {}
    for key, value in d.items():
        if value >= minimum:
            d2[key] = value

    return d2

print(filter_by_value({"Ana": 15, "Ben": 9}, 10))
