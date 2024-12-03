def First_Negative_Number(arr_, n):
    length = len(arr_) - n
    for i in range(len(arr_)):

        if i + n <= len(arr_):
            list2 = arr_[i:i + n]


Array = [12, -1, -7, 8, -15, 30, 16, 28]
window_size = 3
Output = First_Negative_Number(Array, window_size)
print(Output)
