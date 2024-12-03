def give_rank(list_):
    dict_index = {}
    medal_string = ['0'] * len(list_)
    medal_list = ['Gold Medal', 'Silver Medal', 'Bronze medal']
    for element in list_:
        dict_index[element] = list_.index(element)
    list_.sort(reverse=True)
    for index__ in range(len(list_)):
        ord_index = dict_index[list_[index__]]
        if index__ < 3:
            medal_string[ord_index] = medal_list[index__]
        else:
            medal_string[ord_index] = str(index__ + 1)
    return medal_string


Rank_list = [10, 3, 8, 9, 4]
Output = give_rank(Rank_list)
print(Output)
