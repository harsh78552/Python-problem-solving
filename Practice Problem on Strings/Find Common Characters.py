def common_character(list_):
    dict_ = {}
    for char in list_[0]:
        if char not in dict_:
            dict_[char] = 1
        else:
            dict_[char] += 1
    for word in list_[1:]:
        dict__ = {}
        for char in word:
            if char not in dict__:
                dict__[char] = 1
            else:
                dict__[char] += 1
        for char1 in list(dict_.keys()):
            if char1 in dict__:
                dict_[char1] = min(dict_[char1], dict__[char1])
            else:
                del dict_[char1]
    result = []
    for key, value in dict_.items():
        for j in range(value):
            result.append(key)
    return result


Input_list = ['bella', 'label', 'roller']
Output = common_character(Input_list)
print(Output)