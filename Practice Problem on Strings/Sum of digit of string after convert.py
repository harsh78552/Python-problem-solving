def conversion(string_):
    string_int = ''
    count_ = 0

    for i in string_:
        string_int += str((ord(i) - 97) + 1)

    while True:
        sum_ = 0
        for j in string_int:
            sum_ += int(j)
        string_int = str(sum_)
        count_ += 1
        if len(string_int) == 1:
            print(string_int)
            break

    return count_


Input_String = 'iiii'

Output = conversion(sorted(Input_String))
print(Output)
