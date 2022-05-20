def convert_num_to_hours_and_minutes(num):
    hour = num // 60
    minutes = num % 60
    if ((hour > 1) or (hour == 0)) and ((minutes > 1) or (minutes == 0)):
        print(hour, "hours" ",", minutes, "minutes")
    elif ((hour == 0) or (hour > 1)) and (minutes == 1):
        print(hour, "hours" ",", minutes, "minute")
    elif (hour == 1) and ((minutes == 0) or (minutes > 1)):
        print(hour, "hour" ",", minutes, "minutes")
    else:
        print(hour, "hour" ",", minutes, "minute")


convert_num_to_hours_and_minutes(71)
