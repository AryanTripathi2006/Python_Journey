# input() = A function that prompts the user to enter data.
#           Returns the entered data as a string.


name = input("What is your name?: ")                                     # input() function take and returns string as input
age = int(input("How old are you?: "))


age = age + 1

print(f"Hello {name}")
print("HAPP BIRTHDAY!")
print(f"you are {age} now")