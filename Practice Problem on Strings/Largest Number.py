def largest_number(list_):
    for j in range(len(list_)):
        num = j
        for k in range(j + 1, len(list_)):
            num1 = int(str(list_[num]) + str(list_[k]))
            num2 = int(str(list_[k]) + str(list_[num]))
            if num1 > num2:
                pass
            else:
                list_[j], list_[k] = list_[k], list_[j]
        if list_[j] == 0:
            return "0"
    return list_


number_list = [3, 30, 34, 5, 9]
# number_list = [0, 0]
test_case = largest_number(number_list)
Num_Str = ""
for num_str in test_case:
    Num_Str += str(num_str)
print(Num_Str)
