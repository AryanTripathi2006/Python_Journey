# logical operators = evaluate multiple conditions (or, and, not)
#                     or = atleast one condition must be True
#                     and = both condition must be True
#                     not = inverts the condition (not False, not True)

# OR operation

# temp = 19
# is_raining = True

# if temp >= 35 or temp <= 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is scheduled")


# AND operation

temp = -1
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside🥵")
    print("It is Sunny☀️")
elif temp >= 10 and temp < 28 and is_sunny:
    print("It is warm outside🌞")
    print("It is Sunny☀️")
elif temp >= 0 and temp < 10 and is_sunny:
    print("It is cold outside🥶")
    print("It is Sunny☀️")
elif temp < 0 and is_sunny:
    print("It is freezing outside❄️")
    print("It is Sunny☀️")
elif temp >= 28 and not is_sunny:
    print("It is hot outside🥵")
    print("It is Cloudy☁️")
elif temp >= 10 and temp < 28 and is_sunny:
    print("It is warm outside🌞")
    print("It is Cloudy☁️")
elif temp >= 0 and temp < 10 and not is_sunny:
    print("It is cold outside🥶")
    print("It is Cloudy☁️")
elif temp < 0 and not is_sunny:
    print("It is freezing outside❄️")
    print("It is Cloudy☁️")
else:
    print("Itcan't be displayed")