## create pyramid using for loop

rows = 6

num = 1

for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
        if num > 20: 
            break

    print()
