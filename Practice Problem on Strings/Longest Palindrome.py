def Palindrome_Length(string_):
    dict_ = {}
    result = 0
    odd_count_present = False

    for char in string_:
        if char not in dict_:
            dict_[char] = 1
        elif char in string_:
            dict_[char] += 1

    for key, value in dict_.items():
        if value % 2 != 0:
            dict_[key] = value - 1
            result += dict_[key]
            odd_count_present = True
        elif value % 2 == 0:
            result += dict_[key]
    if odd_count_present:
        return result + 1
    return result


Input_String = 'aabbcc'
Output = Palindrome_Length(Input_String)
print(Output)
