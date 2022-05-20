celsius = int(input())
fahrenheit = int(input())


def celsius_to_fahrenheit(celsius):
    temp_in_fahrenheit = (celsius * 9 / 5) + 32
    return temp_in_fahrenheit


print(celsius_to_fahrenheit(celsius))


def fahrenheit_to_celsius(fahrenheit):
    temp_in_celsius = (fahrenheit - 32) * 5 / 9
    return temp_in_celsius


print(fahrenheit_to_celsius(fahrenheit))
