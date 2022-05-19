def maximum(
    a,
    b,
    c,
):
    if (a > b) and (a > c):
        max = a
    elif (b > a) and (b > c):
        max = b
    elif (c > a) and (c > b):
        max = c
    return max


print(
    maximum(
        10,
        80,
        3,
    )
)
