def Score_Of_String(string__):
    score_sum = 0
    for i in range(len(string__)):
        if i + 1 < len(string__):
            score_sum += abs(ord(string__[i]) - ord(string__[i + 1]))
    return score_sum


Input_String = 'harsh'
Output = Score_Of_String(Input_String)
print(Output)
