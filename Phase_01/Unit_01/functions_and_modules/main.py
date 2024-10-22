import random


def adder(num1: int, num2: int) -> int:
    random_int = random.randint(1, 10)
    return num1 + num2 + random_int


int_var = 24
result = adder(int_var, 3)

print(result)
