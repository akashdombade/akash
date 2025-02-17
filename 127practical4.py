# if statement
print("if statement:")
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
print("\nif-else statement:")
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# if-elif-else statement
print("\nif-elif-else statement:")
z = 7
if z > 10:
    print("z is greater than 10")
elif z == 7:
    print("z is equal to 7")
else:
    print("z is less than 7")

# Nested if statement
print("\nNested if statement:")
a = 20
b = 15
if a > 10:
    print("a is greater than 10")
    if b > 10:
        print("b is also greater than 10")
    else:
        print("b is less than or equal to 10")
else:
    print("a is less than or equal to 10")
