def great_string(str__):
    j = 0
    list__ = [str__[j]]

    for i in range(1, len(str__)):
        if len(list__) > 0:
            if abs(ord(list__[j]) - ord(str__[i]) == 32):
                list__.pop()
                j -= 1
                continue
        list__.append(str__[i])
        j += 1
    return list__


Input = 'abBAcC'
Output = great_string(Input)
print(Output)
