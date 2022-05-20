x = input("degrees celcius:")


def celsius_to_fahrenheit(x):  # where x is degrees celcius
    temp_in_fahrenheit = (x * 9 / 5) + 32
    return temp_in_fahrenheit


y = input("degrees fahrenheit:")


def fahrenheit_to_celsius(y):
    temp_in_celsius = (y - 32) * 5 / 9  # where y is degrees fahrenheit
    return temp_in_celsius
