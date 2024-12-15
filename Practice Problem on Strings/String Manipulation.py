def Senior_Citizen(details_):
    passenger_count = 0
    for i in details_:
        if len(i) == 15:
            age = i[-3:-5:-1]
            if int(age[-1::-1]) > 60:
                passenger_count += 1
            else:
                pass
        else:
            print(f"Condition not match.... at index {details_.index(i)}.")
    return f"{passenger_count} passenger's are strictly above then 60."


Input_details = ['7868190130M7522', '5303914400F9211', '9273338290F4010', '12']
Output = Senior_Citizen(Input_details)
print(Output)
