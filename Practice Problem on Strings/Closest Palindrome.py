def closest_palindrome(string_):
    reverse_string = ''
    for char in string_:
        reverse_string = char + reverse_string
    if len(string_) < 2 and int(string_) > 0:
        return int(string_) - 1
    elif string_ == reverse_string:
        if 9 * (int(len(string_) * '1')) == int(string_):
            return 10 ** len(string_) + 1
        elif len(string_) > 3:
            half_length = len(string_) // 2
            collect_num = int(string_[0:half_length]) - 1
            return f'{collect_num}{str(collect_num)[half_length::-1]}'
        elif len(string_) == 2:
            half_length = len(string_) // 2
            collect_num = int(string_[half_length]) - 1
            return f'{str(collect_num) * 2}'
        else:
            half_length = len(string_) // 2
            return f'{string_[0:half_length]}{int(string_[half_length]) - 1}{string_[0:half_length]}'
    elif len(string_) % 2 != 0:
        if 10 ** (len(string_) - 1) == int(string_):
            return f'{10 ** (len(string_) - 1) - 1}'
        elif len(string_) == 3:
            half_length = len(string_) // 2
            return f'{string_[0:half_length]}{int(string_[half_length]) + 1}{string_[0:half_length]}'
        else:
            half_length = len(string_) // 2
            return f'{string_[0:half_length]}{int(string_[half_length]) + 1}{string_[half_length - 1::-1]}'

    elif len(string_) % 2 == 0:
        if 10 ** (len(string_) - 1) == int(string_):
            return f'{10 ** (len(string_) - 1) - 1}'


Input_string = input('Enter string only in form of number:')
Output = closest_palindrome(Input_string)
print(Output)
