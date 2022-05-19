num = int(input("enter minutues:"))


def convert_num_to_hours_and_minutes(num):
    hour = num // 60
    minutes = num % 60
    if (hour > 1) and (minutes > 1):
        print(hour, "hours" ",", minutes, "minutes")
    elif (hour > 1) and (minutes == 1):
        print(hour, "hours" ",", minutes, "minute")
    elif (hour > 1) and (minutes == 0):
        print(hour, "hours" ",", minutes, "minutes")
    elif (hour == 0) and (minutes > 1):
        print(hour, "hours" ",", minutes, "minutes")  # grammatically we say 0 hours
    elif (hour == 0) and (minutes == 0):
        print(hour, "hours" ",", minutes, "minutes")  # grammmatically we say 0 minutes
    elif (hour == 0) and (minutes == 1):
        print(hour, "hours" ",", minutes, "minute")
    elif (hour <= 1) and (minutes > 1):
        print(hour, "hour" ",", minutes, "minutes")
    elif (hour <= 1) and (minutes == 1):
        print(hour, "hour" ",", minutes, "minute")
    else:
        print(hour, "hour" ",", minutes, "minutes")


convert_num_to_hours_and_minutes(num)
