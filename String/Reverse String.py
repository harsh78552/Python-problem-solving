def Reverse_String(string__):
    reverse_string_list = []
    if len(string__) < 2:
        return string__
    else:
        for i in range(1, len(string__) + 1):
            reverse_string_list.append(string__[-i])
    return reverse_string_list


Input_String = ['h', 'e', 'l', 'l', 'o', 'k', 'l']
Output = Reverse_String(Input_String)
print(Output)
