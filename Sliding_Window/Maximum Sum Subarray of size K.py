def max_subarray(arr_, length, n):
    loop_run = length - n
    sum_ = arr_[0] + arr_[1] + arr_[2]
    max_sum = sum_
    for i in range(1, loop_run + 1):
        sum_ = sum_ - arr_[i] + arr_[i + n - 1]
        if max_sum < sum_:
            max_sum = sum_
    return max_sum


Array = [100, 200, 50, 0, 200, 200, 100]
Length = len(Array)
window_size = 3
Output = max_subarray(Array, Length, window_size)
print(Output)
