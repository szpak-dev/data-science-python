def average_dict_values(data):
    return sum(data.values()) / len(data)


data = {'a': 100, 'b': 120, 'c': 130}
average = average_dict_values(data)

print(average)
