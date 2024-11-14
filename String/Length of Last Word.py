def length_last_word(string_):
    length = 0
    for _ in string_[-1]:
        length += 1
    return length


Input_String = input("Enter string: ").split()
Output = length_last_word(Input_String)
print(Output)
