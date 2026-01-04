"""
Python Programming Lab Report – Lab 01
=========================================

Student Name : Dinesh Basnet
Lab Title    : Introduction to Python Basics

OBJECTIVE
-----------------------------------------
1. To understand basic data types in Python
2. To learn loops and range function
3. To understand mutable and immutable data types
4. To use input() and type casting
5. To define and use functions

THEORY
-----------------------------------------
Python is a high-level, interpreted programming language.
It supports various built-in data types.

Mutable data types:
- List
- Dictionary
- Set

Immutable data types:
- int
- float
- string
- tuple

The input() function always takes input as a string.
Type casting is required for numerical operations.
"""

# 1. BASIC DATA TYPES
# ---------------------------------------

a = 10                 # int
b = 99.99              # float
c = 3 + 4j             # complex
s = "python"           # string
l = [4, 5, 6]          # list
t = (1, 2, 3)          # tuple
j = {1, 2, 3}          # set
i = True               # boolean
d = {"Name": "Jay Prakash", "id": 15}  # dictionary

# 2. LOOP THROUGH LIST
# ---------------------------------------

print("Elements of list:")
for item in l:
    print(item)

# 3. RANGE FUNCTION
# ---------------------------------------

print("\nEven numbers from 0 to 8:")
for num in range(0, 10, 2):
    print(num)

# 4. TYPE CHECKING
# ---------------------------------------

print("\nData Types:")
print(type(a))
print(type(b))
print(type(d))
print(type(t))

# 5. INPUT FUNCTION
# ---------------------------------------

name = input("\nEnter your name: ")
print(f"Hello {name}")

# 6. TYPE CASTING
# ---------------------------------------

a = input("\nEnter a number: ")
b = input("Enter another number: ")
print("Without type casting (string):", a + b)

c = int(input("Enter a number: "))
d = int(input("Enter another number: "))
print("With type casting (int):", c + d)

# 7. FUNCTION EXAMPLE
# ---------------------------------------

def area_rectangle(x, y):
    """
    This function calculates area of rectangle
    """
    return x * y

print("\nArea of rectangle:", area_rectangle(4, 5))

"""
RESULT
-----------------------------------------
All programs executed successfully and
basic Python concepts were understood.

CONCLUSION
-----------------------------------------
This lab provides a strong foundation in
Python programming and prepares for
advanced topics like backend development.
"""


