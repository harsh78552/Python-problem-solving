from datetime import datetime


def time_comparison(time_list):
    list1 = []
    list2 = []
    minute_list = []
    list__ = []
    for j in time_list:
        time_object = datetime.strptime(j, "%H:%M")
        hour = time_object.hour
        list1.append(hour)
        minute = time_object.minute
        list2.append(minute)

    for len_ in range(len(list1)):

        minute_ = list1[len_] * 60 + list2[len_]
        if minute_ == 0:
            minute_list.append(24 * 60)
        else:
            minute_list.append(minute_)
    ref = sorted(minute_list)
    print(ref)

    for len__ in range(len(ref) - 1):
        print(ref[len__], ref[len__+1])
        x = abs(ref[len__] - ref[len__ + 1])
        list__.append(x)
    return min(list__)


Time_List = ['00:00', '23:59', '13:21', '01:10', '13:24']
Output = time_comparison(Time_List)
print(Output)
