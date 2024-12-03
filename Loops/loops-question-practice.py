# Beginner-Level Questions
""""""


# 1.Print Numbers from 1 to 10
def Print_Number():
    for i in range(1, 11):
        print(i)


Print_Number()


# 2.Sum of Natural Numbers
def sum_natural_numbers(num1):
    natural_number_sum = 0
    for i in range(1, num1 + 1):
        natural_number_sum += i
    return natural_number_sum


Input = int(input("Enter stopping number: "))
Output = sum_natural_numbers(Input)
print(Output)


# 3.Find All Divisors of a Number
def Find_Divisor(num1):
    dict_ = {}
    list_ = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            list_.append(i)
    dict_[num1] = list_
    return dict_


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


# 7.Factorial of a Number
def Factorial(num_):
    factorial = 1
    for i in range(1, 5 + 1):
        factorial *= i
    return factorial


Input = int(input("Enter number: "))
Output = Factorial(Input)
print(Output)


# 8.Reverse a Practice Problem on Strings
def Reverse_string(str_):
    # This function just revere string
    str__ = ''
    for i in str_:
        str__ = i + str__
    return str__


print(Reverse_string.__doc__)
Input = input("Enter string: ")
Output = Reverse_string(Input)
print(Output)


# 9.Check for Prime Numbers
def check_prime(num_):
    is_prime = True
    for i in range(2, num_):
        if num_ % i == 0:
            is_prime = False
            break
    if not is_prime:
        return "Composite number..."
    else:
        return "Prime number..."


Input = int(input("Enter number: "))
Output = check_prime(Input)
print(Output)


# 10.Fibonacci Series
def Fibonacci_Series(num):
    zero = 0
    one = 1
    print(zero)
    print(one)
    for i in range(1, num + 1):
        fibonacci = zero + one
        zero = one
        one = fibonacci
        print(fibonacci)


Input = int(input("Enter stopping number: "))
Fibonacci_Series(Input)


# 11.Find the Maximum and Minimum in a List
def Find_Max(list_):
    max_ = list_[0]
    min_ = list_[0]
    for i in range(len(list_)):
        if max_ < list_[i]:
            max_ = list_[i]
        elif min_ > list_[i]:
            min_ = list_[i]
    return f"{max_} is maximum in list...\n{min_} is minimum in list... "


Input = [1, 4, 5, 2, 3, 8, 1, 34, 100]
Output = Find_Max(Input)
print(Output)


# 12.Number of Occurrences of Each Character
def character_occurrence(str_):
    dict_ = {}
    value = 1
    for char in str_:
        if char not in dict_:
            dict_[char] = value
        elif char in dict_:
            dict_[char] += value
    return dict_


Input = input("Enter Practice Problem on Strings: ").replace(" ", "")
Output = character_occurrence(Input)
print(Output)
