# Dictionary: Comma separated key-value pairs enclosed within {}.
# Each key value pair is separated by : {key1:value1, key2:value2,.......}
# Ordered, Mutable, Duplicacy not allowed

groceries = {"milk": 40, "biscuit": 60, "rice": 90, "bread": 90}
# print(groceries, type(groceries))
# print(len(groceries))                    # Gives the number of key:value pairs
# print(groceries[0])                      # It does not have indexes
# print(groceries["milk"])                 # Every key is associated with value therfore rather than indexes we use key to fetch the value associated with that key.

# Dictionaries are mutable 
# groceries["milk"] = 45                   # updates the value of the key
# groceries["eggs"] = 10                   # adds new key-value pair to the dictionary
# print(groceries)



Student1 = {"maths": 80.5, "English": 76.0, "Physics": 89.0}
# print(Student1)
# print(Student1["Physics"])               # Fetch the value of Physics


# get(): fetches the value of key
# Syntax: variable.get("key")

# print(Student1.get("Physics"))
# print(Student1.get("Chem"))              # No error instead give "None" as output
# print(Student1.get("Chem", 40))          # Sets the default value of Chemistry as 40 since it is not present in the dictionary, doesnot update the dictionary.


# emp1 = {'id': 1001, 'name': 'John', 'salary': 10000}
# print(emp1.get('phone_num', 9876543210)) # Since the key is not present therfore Prints default value
# print(emp1.get('id', 9876543210))        # Prints the value associated with the key


# Membership Operator
# print("name" in emp1)                    # Checks the key in dictionary

# update(): updates the key value pair of another dictionary inside the existing dictionary.
# Syntax: dict1.update(dict2)

# sem1_marks = {'maths': 78.5, 'eng': 71.0, 'phy': 86.5}
# sem2_marks = {'chem': 81.5, 'bio': 90.5}

# sem1_marks.update(sem2_marks)             # updates the key value pair of another dictionary inside the existing dictionary.
# print(sem1_marks)

# groceries_1 = {'milk': 60, 'rice': 100, 'biscuits': 20}
# groceries_2 = {'rice': 110, 'bread': 55}
# groceries_1.update(groceries_2)
# print(groceries_1)

# pop(): to remove key value pair
# syntax: dictionary.pop('key')
# groceries_1.pop('milk')
# print(groceries_1)

# groceries_1 = {'milk': 60, 'rice': 100, 'biscuits': 20, 'milk': 65}
# Keys cannot be duplicated in a dict and the value should be the most recent value


d1 = {{'a': 1}: 6,{'b': 2}: 12}
print(d1)


# keys allowed: str, int, float, bool, tuples
# Keys not allowed: list, set