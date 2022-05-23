def maximum(value_1, value_2, value_3):
    if (value_1 >= value_2) and (value_1 >= value_3):
        largest = value_1
    elif value_2 >= value_3:
        largest = value_2
    else:
        largest = value_3
    return largest


print(maximum(1, 1, 0))
