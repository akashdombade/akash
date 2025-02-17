# While loop
print("While loop:")
i = 1
while i <= 5:  # Loop runs while i is less than or equal to 5
    print(f"Iteration {i}")
    i += 1  # Increment i to avoid infinite loop

# For loop
print("\nFor loop:")
for j in range(1, 6):  # Loop through numbers from 1 to 5
    print(f"Iteration {j}")

# Nested loop
print("\nNested loop:")
for x in range(1, 4):  # Outer loop runs 3 times
    for y in range(1, 4):  # Inner loop runs 3 times for each iteration of the outer loop
        print(f"Outer loop iteration {x}, Inner loop iteration {y}")
