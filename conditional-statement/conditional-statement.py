# Find the largest number
""""""
"""def find_largest(input_, input__, input___):
    if input__ < input_ > input___:
        return f'{input_} is greater...'
    elif input_ < input__ > input___:
        return f'{input__} is greater...'
    else:
        return f'{input___} is greater...'


Input_ = int(input("Enter first number:"))
Input__ = int(input("Enter first number:"))
Input___ = int(input("Enter first number:"))
Output = find_largest(Input_, Input__, Input___)
print(Output)"""

# Check if a number is positive, negative, or zero.
"""def integer_type(input_):
    if input_ > 0:
        return 'Positive number...'
    elif input_ == 0:
        return 'Zero...'
    else:
        return 'negative number...'


Input = int(input("Enter number: "))
Output = integer_type(Input)
print(Output)"""

# Check if a number is a leap year.
"""def leap_year(input_year):
    if (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0:
        return 'Leap year...'
    else:
        return 'Not...'


Input_year = int(input('Enter year: '))
Output = leap_year(Input_year)
print(Output)"""

# Check if a number is a perfect number.
"""def perfect_number(num1):
    sum_ = 0
    for i in range(1, num1):
        if num1 % i == 0:
            sum_ += i
    if sum_ == num1:
        return 'Perfect number...'
    else:
        return 'Not a perfect number...'


Input = int(input("Enter number:"))
Output = perfect_number(Input)
print(Output)"""

# Check if a number is prime.
"""def check_prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if not is_prime:
        return 'Prime number...'
    elif is_prime:
        return 'Not prime...'


Input_number = int(input("Enter number: "))
Output = check_prime(Input_number)
print(Output)"""

# Check if a string is a palindrome.
"""def check_palindrome(str_):
    str__ = ''.strip()
    for i in str_:
        str__ = i + str__
    if str__ == str_:
        return 'string is palindrome...'
    else:
        return 'not palindrome...'


Input_ = input("Enter string: ").strip()
Output = check_palindrome(Input_)
print(Output)"""

# Find the second-largest number in a list.
"""def second_largest_num(list_):
    for num in range(len(list_)):
        min_index = num
        for num1 in range(num + 1, len(list_)):
            if list_[min_index] < list_[num1]:
                min_index = num1
        list_[num], list_[min_index] = list_[min_index], list_[num]
    return f"{list_[1]} is second largest number..."


Input = [1, 2, 4, 6, 8, 9, 10, 6, 18]
Output = second_largest_num(Input)
print(Output)"""

# Check if a number is an Armstrong number.
"""def check_armstrong_number(Input_):
    length = len(Input_)
    sum_ = 0
    for i in Input_:
        sum_ += int(i) ** length
    if sum_ == int(Input_):
        return 'Armstrong number...'
    else:
        return 'Not armstrong number...'


Input = input("Enter your number: ")
Output = check_armstrong_number(Input)
print(Output)"""


# Check if a string contains vowels or not.
def check_vowels(str_):
    vowel_ = 'a,e,i,o,u'
    for i in vowel_:
        if i in str_:
            return 'String contain vowel...'
    return 'String not contain vowel...'


Input = input("Enter string: ").lower()
Output = check_vowels(Input)
print(Output)
