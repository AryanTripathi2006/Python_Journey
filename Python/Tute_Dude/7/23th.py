# Dictionary: Comma separated key-value pairs enclosed within {}.
# Each key value pair is separated by : {key1:value1, key2:value2,.......}
# Ordered, Mutable, 

groceries = {"milk": 40, "biscuit": 60, "rice": 90, "bread": 90}
# print(groceries, type(groceries))
# print(len(groceries))               # Gives the number of key:value pairs
# print(groceries[0])                 # It does not have indexes
# print(groceries["milk"])            # Every key is associated with value therfore rather than indexes we use key to fetch the value associated with that key.

# Dictionaries are mutable 
groceries["milk"] = 45              # updates the value of the key
groceries["eggs"] = 10              # adds new key-value pair to the dictionary
print(groceries)