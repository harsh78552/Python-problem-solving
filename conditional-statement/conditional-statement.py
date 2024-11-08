# Find the largest number
def find_largest(input_, input__, input___):
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
print(Output)
