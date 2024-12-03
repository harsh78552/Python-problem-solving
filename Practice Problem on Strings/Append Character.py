def Solution(string1, string2):
    i = 0
    j = 0
    while i < len(string1) and j < len(string2):
        if string2[j] == string1[i]:
            i += 1
            j += 1
        elif string2[j] != string1[i]:
            i += 1
    return abs(j - len(string2))


Input_String = 'coaching'
Input_String2 = 'coding'
Output = Solution(Input_String, Input_String2)
print(Output)
