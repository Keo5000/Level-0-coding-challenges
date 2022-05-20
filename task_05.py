side_1 = int(input())
side_2 = int(input())
side_3 = int(input())


def area_of_triangle(side_1, side_2, side_3):
    semi_parameter = (side_1 + side_2 + side_3) / 2
    area = (
        semi_parameter
        * (semi_parameter - side_1)
        * (semi_parameter - side_2)
        * (semi_parameter - side_3)
    ) ** 0.5
    return area
