# 1.Pattern--->A
for row in range(7):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (0 < col < 4)):
            print('*', end=" ")
        else:
            print(end='  ')
    print()
