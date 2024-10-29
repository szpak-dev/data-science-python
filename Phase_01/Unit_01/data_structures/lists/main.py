def some_function(arg1: str, the_list: list):
    the_list.append('abc')

numbers = [1, 2, 3, 4, 5]

# access / read
first_element = numbers[0]
last_element = numbers[-1]
subset = numbers[1:4]
# print(subset)

# access / write
strings = ['apple', 'banana', 'cherry', 'avocado']
strings.extend(['carrot', 'dill'])

print(strings)