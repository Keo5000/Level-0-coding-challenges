value_1 = int(input())
value_2 = int(input())
value_3 = int(input())

def maximum(value_1, value_2, value_3):
    if (value_1 > value_2) and (value_1 > value_3):
        largest = value_1
    elif (value_2 > value_1) and (value_2 > value_3):
        largest = value_2
    elif (value_3 > value_1) and (value_3 > value_2):
        largest = value_3
    return largest


print(maximum(value_1, value_2, value_3))
