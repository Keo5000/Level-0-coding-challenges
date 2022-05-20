a = int(input("side 1:"))
b = int(input("side 2:"))
c = int(input("side 3:"))


def area_of_triangle(a, b, c):  # where a, b and c are the sides of the triangle)
    s = (a + b + c) / 2  # semi-parameter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

