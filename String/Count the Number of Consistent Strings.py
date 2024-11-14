def count_(allowed_, words_):
    set_ = set()
    count__ = 0
    for i in allowed_:
        set_.add(i)
    for j in words_:
        check_ = True
        for k in j:
            if k not in set_:
                check_ = False
                break
        if check_:
            count__ += 1
    return count__


allowed = 'abc'
words = ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
Output = count_(allowed, words)
print(Output)
