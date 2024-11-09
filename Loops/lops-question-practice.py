# Beginner-Level Questions
""""""


# 1.Print Numbers from 1 to 10

def Print_Number():
    for i in range(1, 11):
        print(i)


Print_Number()


# 2.Sum of Natural Numbers

def sum_natural_numbers(num1):
    """ This function find sum of natural
            number start from 1 and stopping number
                insert through user."""
    natural_number_sum = 0
    for i in range(1, num1 + 1):
        natural_number_sum += i
    return natural_number_sum


print(sum_natural_numbers.__doc__)
Input = int(input("Enter stopping number: "))
Output = sum_natural_numbers(Input)
print(Output)


# 3.Find All Divisors of a Number
def Find_Divisor(num1):
    """This function find all numbers which is
          divisor of user input number."""
    dict_ = {}
    list_ = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            list_.append(i)
    dict_[num1] = list_
    return dict_


print(Find_Divisor.__doc__)
Input = int(input("Enter number: "))
Output = Find_Divisor(Input)
print(Output)


# 4.Armstrong Numbers in a Range
def Armstrong_Number(num_):
    list_ = []
    for i in range(1, num_ + 1):
        num_str = str(i)
        length = len(str(i))
        sum_ = 0
        for j in num_str:
            sum_ += int(j) ** length
        if i == sum_:
            list_.append(sum_)
    return list_


Input = int(input("Enter stopping number:"))
Output = Armstrong_Number(Input)
print(Output)


# 5.Transpose of a Matrix
def Matrix_Transpose(matrix_):
    if len(matrix_) <= 1:
        return matrix_
    else:
        list__ = []
        for i in range(len(matrix_[0])):
            list_ = []
            for j in range(len(matrix_)):
                list_.append(matrix_[j][i])
            list__.append(list_)
    return list__


Matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
Output = Matrix_Transpose(Matrix)
print(Output)


# 6.Flatten a Nested List
def Flatten_List(input_):
    list_ = []
    for i in input_:
        for j in i:
            list_.append(j)
    return list_


List = [[1, 2], [3, 4], [5, 6]]
Output = Flatten_List(List)
print(Output)
