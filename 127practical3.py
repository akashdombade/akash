# arithmatic operator # Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:")
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation
print(f"a // b = {a // b}")  # Floor Division

# Relational Operators
print("\nRelational Operators:")
print(f"a == b: {a == b}")  # Equal to
print(f"a != b: {a != b}")  # Not equal to
print(f"a > b: {a > b}")    # Greater than
print(f"a < b: {a < b}")    # Less than
print(f"a >= b: {a >= b}")  # Greater than or equal to
print(f"a <= b: {a <= b}")  # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print(f"x and y: {x and y}")  # AND
print(f"x or y: {x or y}")    # OR
print(f"not x: {not x}")      # NOT

# Assignment Operators
print("\nAssignment Operators:")
x = 10
print(f"x = {x}")
x += 5
print(f"x += 5: {x}")  # Add and assign
x -= 3
print(f"x -= 3: {x}")  # Subtract and assign
x *= 2
print(f"x *= 2: {x}")  # Multiply and assign
x /= 4
print(f"x /= 4: {x}")  # Divide and assign
x %= 3
print(f"x %= 3: {x}")  # Modulus and assign

# Bitwise Operators
print("\nBitwise Operators:")
a = 10  # In binary: 1010
b = 4   # In binary: 0100
print(f"a & b: {a & b}")  # AND
print(f"a | b: {a | b}")  # OR
print(f"a ^ b: {a ^ b}")  # XOR
print(f"a << 1: {a << 1}")  # Left shift
print(f"a >> 1: {a >> 1}")  # Right shift

# Membership Operators
print("\nMembership Operators:")
lst = [1, 2, 3, 4, 5]
print(f"3 in lst: {3 in lst}")  # Check if 3 is in list
print(f"6 not in lst: {6 not in lst}")  # Check if 6 is not in list

# Identity Operators
print("\nIdentity Operators:")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x is y: {x is y}")    # Check if x and y refer to the same object
print(f"x is z: {x is z}")    # Check if x and z refer to the same object
print(f"x is not y: {x is not y}")  # Check if x and y do not refer to the same object
