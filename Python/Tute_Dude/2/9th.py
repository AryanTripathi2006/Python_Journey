# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Select the unit of your weight (K or L): ")

if unit == "kg":
    result = weight * 2.20462262
    print(f"Your weight in pounds is {round(result, 3)}lbs")
elif unit == "lbs":
    result = weight / 2.20462262
    print(f"Your weight in pounds is {round(result, 3)}kgs")
else:
    print(f"{unit} is an invalid input of unit")