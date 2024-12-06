def make_palindrome(string_):
    dict_ = {}
    if len(string_) < 1:
        return string_
    else:
        for i in string_:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1

        for key, value in dict_.items():
            if value % 2 != 0:
                dict_[key] = value - 1

        initialise_list = [None] * (sum(list(dict_.values())) + 1)
        count_ = 0
        count1 = len(initialise_list) - 1

        for key1, value1 in dict_.items():
            if value1 == 0:
                initialise_list[len(initialise_list) // 2] = key1
            else:
                for k in range(value1 // 2):
                    if count_ <= count1:
                        initialise_list[count_] = key1
                        initialise_list[count1] = key1
                        count_ += 1
                        count1 -= 1
    string__ = ''.join(initialise_list)
    return f"Palindrome of input string is: {string__}"


Input_String = 'abbcdccac'
sorted_str = ''.join(sorted(Input_String))
Output = make_palindrome(sorted_str)
print(Output)
