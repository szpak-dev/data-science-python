# Activity 1: Create a list of numbers and a list of strings
numbers = [1, 2, 3, 4, 5]
strings = ["apple", "banana", "cherry"]

# Activity 2: Access first and last elements, slice the list
first_element = numbers[0]
last_element = numbers[-1]
subset = numbers[1:4]

# Activity 3: Add and remove elements from a list of fruits
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.extend(["grape", "mango"])
fruits.remove("banana")
popped_fruit = fruits.pop(2)
del fruits[0]

# Activity 4: Iterate through a list of student names
students = ["Alice", "Bob", "Charlie"]
for index, student in enumerate(students):
    print(f"{index}: {student}")

# Activity 5: Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Activity 6: Use sort, reverse, find min and max in a list
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
numbers.reverse()
min_value = min(numbers)
max_value = max(numbers)

# Activity 7: Grocery list simulation
grocery_list = ["milk", "eggs", "bread", "butter"]
grocery_list.append("cheese")
grocery_list.remove("bread")
grocery_list.sort()
for item in grocery_list:
    print(f"Bought: {item}")
