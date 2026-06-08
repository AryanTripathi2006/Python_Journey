# Python temperature converter

unit = input("Enter the unit of temperature (C / F / K): ")
temp = float(input("Enter the temperature: "))

if unit.lower() == "c":
    temp1 = temp * 9/5 + 32
    print(f"Temperature in Faherenheit is: {temp1}°F")
    temp = temp + 273.2
    print(f"Temperature in Kelvin is: {temp}k")
elif unit.lower() == "f":
    temp1 = (temp - 32)*5/9
    print(f"Temperature in Celcius is: {temp1}°C")
    temp = temp1 + 273.2
    print(f"Temperature in Kelvin is: {temp}k")
elif unit.lower() == "k":
    temp1 = temp - 273.2
    print(f"Temperature in Celcius is: {temp1}°C")
    temp = temp1 * 9/5 + 32
    print(f"Temperature in Fahrenheit is: {temp}°F")
else:
    print(f"{unit} is an invalid unit of temperature")