### **Introduction to Python for Data Science (10-15 min)**

---

#### **Why Python is Popular in Data Science?**
Python's popularity in data science comes from its:
- **Simplicity & Readability**: Python’s syntax is straightforward, making it easy to write and read.
- **Vast Ecosystem of Libraries**: Libraries like `NumPy`, `Pandas`, `Scikit-learn`, `Matplotlib`, and `TensorFlow` provide powerful tools for data manipulation, analysis, and machine learning.
- **Community & Support**: A large community of developers and data scientists creates abundant resources, tutorials, and tools.
- **Integration with Other Technologies**: Python integrates well with databases, web applications, and cloud services, which is useful for full-stack data science solutions.

---

#### **Basic Python Syntax Overview**

1. **Variables and Assignment**

Variables store data values. You don't need to declare the type of variable beforehand.

```python
# Assigning values to variables
x = 5           # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True  # Boolean

# Printing variables
print(x, y, name, is_active)
```

2. **Data Types**

- **Integer**: Whole numbers, e.g., `1, 42, -7`
- **Float**: Decimal numbers, e.g., `3.14, 0.001`
- **String**: Text enclosed in quotes, e.g., `"hello", 'world'`
- **Boolean**: True/False values, e.g., `True, False`

```python
# Check data types
print(type(x))       # int
print(type(y))       # float
print(type(name))    # str
print(type(is_active))  # bool
```

---

#### **Basic Operations**

1. **Arithmetic Operations**

Python allows basic mathematical operations on numbers.

```python
# Arithmetic operations
a = 10
b = 4

addition = a + b        # 14
subtraction = a - b     # 6
multiplication = a * b  # 40
division = a / b        # 2.5 (float division)
modulus = a % b         # 2 (remainder)
exponent = a ** b       # 10^4 = 10000
```

2. **String Operations**

Strings are a sequence of characters. They can be manipulated using basic operations.

```python
# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# String repetition
repeat = "Hi!" * 3  # "Hi!Hi!Hi!"

# Accessing characters
first_char = name[0]  # 'A'
```

3. **Boolean Operations**

Logical operations help in decision-making.

```python
# Boolean logic
is_greater = a > b         # True
is_equal = a == b          # False
is_active = not is_active  # False (negation)

# Combining conditions
result = a > b and is_active  # False
```

---

#### **Conclusion**
- Python’s simplicity and powerful libraries make it a preferred language in data science.
- Understanding basic syntax and operations is the first step toward using Python effectively in real-world data science tasks.
