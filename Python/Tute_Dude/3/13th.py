# String Functions
# name = input("Enter your full name: ")

# result = len(name)                                           # len() function is used to return the length of a string (returns an integer value).
# result = name.find("t")                                      # .find("") function is used to find the first appearance of any letter in the string. Returns the index value of that letter.
# result = name.rfind("s")                                     # .rfind("") function is used to find the first appearance of any letter in the string from last(or last occuerence of the letter). Returns the index value of that letter.
#                                                              # if .find("") or .rfind("") cannot find the given letter in a string it would return -1.
# result = name.capitalize()                                   # .capitalize() capitalizes the first letter of the string
# result = name.upper()                                        # .upper() takes all the letter of the string and makes them uppercase.
# result = name.lower()                                        # .lower() takes all the letter of the string and makes them lowercase.
# result = name.isdigit()                                      # only returns true if the string contains "only" digits.
# result = name.isalpha()                                      # only returns true if the string contains "only" alphabetical characters (excludes space also).
# result = name.count("a")                                     # returns an integer. Counts the appearance of a letter in a string.
# result = name.replace("A", " ")                              # replaces "A" with " ".

# print(result)

# phone_num = input("Enter your phone number: ")

# result = phone_num.count(" ")
# result = phone_num.replace("-", " ")

# print(result)

# print(help(str))                                             # to get the comprehensive list of all of the string method.



# Validate user input exercise
# 1. username is no more than 12 characters.
# 2. username must not contain spaces.
# 3. username must not contain digits

user_name = input("Enter a name: ")

if len(user_name) > 12:
    print("Your username cannot be more than 12 characters!")
elif not user_name.isalpha():
    print("Your username cannot contain space or digits")
else:
    print(f"Welcome {user_name}!")