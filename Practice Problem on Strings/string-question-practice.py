# 1.Count Vowels in a Practice Problem on Strings
""""""

"""def count_vowels(str_, vowel_list_):
    dict_ = {}

    for i in vowel_list_:
        count = 0
        for j in str_:
            if i == j:
                count += 1
        dict_[i] = count
    return dict_


Input_string = input("Enter string: ").replace(" ", "").lower()
list_ = ['a', 'e', 'i', 'o', 'u']
Output = count_vowels(Input_string, list_)
print(Output)"""


# 2.Find the First Non-Repeating Character
"""def count_first_non_repeating_character(str_):
    dict_ = {}
    for i in str_:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1
    for key, value in dict_.items():
        if value == 1:
            return key
    return None


Input = "Swiss".lower()
Output = count_first_non_repeating_character(Input)
print(Output)"""

# 3.Count Occurrences of a Character
"""def count_specific_character(str_, char_):
    dict_ = {}
    for char in str_:
        if char not in dict_:
            dict_[char] = 1
        else:
            dict_[char] += 1
    if char_ in dict_.keys():
        return dict_[char_]
    return "character not exist..."


Input = 'hello world'.replace(" ", "")
Input_char = input("Enter a character: ")
Output = count_specific_character(Input, Input_char)
print(Output)"""

# 4.character consecutive count
"""def count_continue_character(string_):
    list_ = []
    count = 0
    first_char = string_[0]
    for k in range(len(string_)):
        if first_char == string_[k]:
            count += 1
        else:
            if count > 1:
                list_.append((first_char, count))
            first_char = string_[k]
            count = 1
    if count > 1:
        list_.append((first_char, count))
    return list_


Input = 'harrrssshhh'
Output = count_continue_character(Input)
print(Output)"""

# 5.Longest Substring Without Repeating Characters
