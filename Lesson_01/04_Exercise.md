### **Hands-on Exercise: Working with a Dataset (10-15 min)**

---

In this hands-on exercise, students will work with a simple dataset, perform basic operations like calculating the mean, sum, and basic statistics using Python libraries like `pandas` and `numpy`.

#### **Objective**:
- Load a dataset into Python using `pandas`.
- Perform basic operations such as calculating means, sums, and descriptive statistics on the dataset.

#### **1. Dataset Setup**
For this exercise, we will use a small CSV dataset. If you don't have a dataset, you can create a simple one manually in a CSV file format (e.g., `data.csv`):

```plaintext
Name, Age, Salary
Alice, 25, 50000
Bob, 30, 60000
Charlie, 35, 55000
David, 40, 70000
Eva, 45, 75000
```

Save this as `data.csv` in your working directory.

---

#### **2. Step-by-Step Instructions**

##### **Step 1: Import Libraries**
First, import the necessary libraries, `pandas` and `numpy`:

```python
import pandas as pd
import numpy as np
```

##### **Step 2: Load the Dataset**
Next, load the dataset from the CSV file using `pandas`:

```python
# Load dataset
df = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print(df.head())
```

This will display the first five rows of the dataset.

##### **Step 3: Perform Basic Operations**

1. **Calculate the Mean of Age and Salary:**

```python
mean_age = df['Age'].mean()
mean_salary = df['Salary'].mean()

print(f"Mean Age: {mean_age}")
print(f"Mean Salary: {mean_salary}")
```

2. **Calculate the Sum of Ages and Salaries:**

```python
sum_age = df['Age'].sum()
sum_salary = df['Salary'].sum()

print(f"Total Age: {sum_age}")
print(f"Total Salary: {sum_salary}")
```

3. **Basic Statistics (Min, Max, Standard Deviation):**

You can easily compute basic statistics using `pandas`:

```python
# Summary statistics for the entire dataset
print(df.describe())

# Specific statistics for Salary
min_salary = df['Salary'].min()
max_salary = df['Salary'].max()
std_salary = df['Salary'].std()

print(f"Min Salary: {min_salary}")
print(f"Max Salary: {max_salary}")
print(f"Salary Standard Deviation: {std_salary}")
```

##### **Step 4: Adding a New Column**
Create a new column, "Bonus," which is 10% of the salary, and add it to the DataFrame:

```python
# Add a new column "Bonus" which is 10% of Salary
df['Bonus'] = df['Salary'] * 0.1
print(df)
```

---

#### **3. Summary of Tasks**

- **Load the dataset** using `pandas`.
- **Calculate basic statistics** such as mean, sum, and standard deviation.
- **Add a new column** to the dataset based on existing data.
