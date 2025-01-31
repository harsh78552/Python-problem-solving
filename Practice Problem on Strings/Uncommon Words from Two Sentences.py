def uncommon_words(string_, string2__):
    dict_ = {}
    dict__ = {}
    uncommon_words_list = []
    for j in string_.split():
        if j not in dict_:
            dict_[j] = 1
        else:
            dict_[j] += 1
    for j in string2__.split():
        if j not in dict__:
            dict__[j] = 1
        else:
            dict__[j] += 1
    for key, value in dict_.items():
        if value == 1:
            if key not in dict__:
                uncommon_words_list.append(key)
    for key, value in dict__.items():
        if value == 1:
            if key not in dict_:
                uncommon_words_list.append(key)

    return uncommon_words_list


String_ = 'no no it is not ok over'
String__ = 'till it is  over'
Output = uncommon_words(String_, String__)
print(Output)
