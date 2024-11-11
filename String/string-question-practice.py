# 1.Count Vowels in a String
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
def count_first_non_repeating_character(str_):
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
print(Output)
