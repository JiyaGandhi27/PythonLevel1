rows = int(input("Enter any number:"))
for i in range(rows):
    for j in range(i + 1):
        print("*", end=' ')
    print("\n")

for i in range(rows, 0, -1):
    for j in range(i - 1):
        print("*", end=' ')
    print("\n")