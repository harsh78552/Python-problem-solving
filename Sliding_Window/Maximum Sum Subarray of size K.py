def max_subarray(arr_, length, n):
    loop_run = length - n
    sum_ = sum(arr_[:n])
    max_sum = sum_
    for i in range(1, loop_run + 1):
        sum_ = sum_ - arr_[i - 1] + arr_[i + n - 1]
        if max_sum < sum_:
            max_sum = sum_
    return max_sum


Array = [100, 200, 50, 0, 200, 20, 100]
Length = len(Array)
window_size = 3
Output = max_subarray(Array, Length, window_size)
print(Output)
