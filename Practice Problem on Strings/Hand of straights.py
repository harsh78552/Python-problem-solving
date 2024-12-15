def replace_word(string_, list_):
    string_list = string_.split()
    string_dict = {}
    for char in string_list:
        for j in range(len(char)):
            jk = char[:j]
            if jk in list_:
                string_dict[char] = jk
                break

    for key, value in string_dict.items():
        if key in string_:
            string_ = string_.replace(key, value)
    return string_


Input_string = 'the cattle was rattled matted by the battery.'
another_list = ['cat', 'bat', 'mat', 'rat']
Output = replace_word(Input_string, set(another_list))
print(Output)
