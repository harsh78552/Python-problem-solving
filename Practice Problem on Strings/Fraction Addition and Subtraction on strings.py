def string_math(string_):
    import math
    i = 0
    list1 = []
    list2 = []
    while i < len(string_):
        current_num = 0
        current_deno = 0
        is_negative = False

        if string_[i] == '-' or string_[i] == '+':
            if string_[i] == '-':
                is_negative = True
            i += 1
        while i < len(string_) and string_[i].isdigit():
            x = int(string_[i])
            current_num = current_num * 10 + x
            i += 1
        if is_negative:
            current_num *= -1
        i += 1
        while i < len(string_) and string_[i].isdigit():
            y = int(string_[i])
            current_deno = current_deno * 10 + y
            i += 1
        list1.append(current_num)
        list2.append(current_deno)
    z = 0
    list2_lcm = math.lcm(*list2)
    for num in range(len(list1)):
        quotient = 6 // list2[num]
        z += quotient * list1[num]
    return f'{z} / {list2_lcm}'


Input_String = '-1/2+1/2+1/3'
Output = string_math(Input_String)
print(Output)
