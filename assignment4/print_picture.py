ROWS = 8

row = ROWS

while row >= 1:
    column = 1

    while column <= row:
        print("*", end="")
        column += 1

    print()
    row -= 1
