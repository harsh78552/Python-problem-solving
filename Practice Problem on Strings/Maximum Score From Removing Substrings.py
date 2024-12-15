def Max_score(string_):
    count_ = 0
    count__ = 1
    j = 0

    while count__ < len(string_):
        if string_[count_] == 'b' and string_[count__] == 'a':
            j += 5

            # print(string_[count_], count_, string_[count__], count__)
        print(string_[count_], count_, string_[count__], count__)

        # elif string_[count_] == 'a' and string_[count__] == 'b':
        #     j += 4

        count_ += 1
        count__ += 1

    return j


Input_String = 'cdbcbbaaabab'
Output = Max_score(Input_String)
print(Output)
