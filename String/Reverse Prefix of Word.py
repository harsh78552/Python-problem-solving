def reverse_string(string_, ch_):
    result = ""
    result1 = ""
    if ch_ not in string_:
        return string_
    else:
        for i in range(len(string_)):
            result = string_[i] + result
            if string_[i] == ch:
                result1 = string_[i + 1:len(string_)]
                break
    return result + result1


String = 'abcddamsghda'
ch = 'd'
Output = reverse_string(String, ch)
print(Output)
