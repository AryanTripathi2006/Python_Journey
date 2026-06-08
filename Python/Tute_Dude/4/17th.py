# Operations on List

# Slicing of List
# l1 = [2,3,1,6,4,7,4,9,8,0,5,8]
# print(l1[2 : 6 : 1])
# print(l1[-5::])

# Concattenation
# l1 = [1, 7, 2]
# l2 = [0, 5]
# print(l1 + l2)
# print(l2 + l1)

# Repetition Operator used by *
# l1 = [1, 7, 2]
# l2 = [0, 5]
# print(l2 * 3)                         # repetition will be in a single list

# Methods of the list

# 1. append = adds only one item / element to end of the list.
# Syntax: list.append(item)

# fruits = ["Mango", "Apple", "Orange"]
# fruits.append("Banana")
# print(fruits)
# print(fruits.append("Banana"))                   # but in this the exisisting list is getting changed or is updated the list functions does not creates a new list.
#                                                                # ^
#                                                                # |
# s1 = "Python is fun"                                           # |
# print(s1.replace("Python", "Java"))              # In this the exisisting string is not getting changed instead a new string gets created by the string functions.


# 2. insert = add an item / element to the specific index within the list. 
# Syntax: list.insert(index, item)

# fruits.insert(2, "Banana")
# print(fruits)


# 3. extend = add items / elements at the end of the list but it can add more than one item / element one by one.
# Syntax: list.extend([item1, item2, ....]).     extend will not add the list as one element instead it will add the items within the list one by one.

# fruits.extend(["Banana", "Guava", "Grapes"])
# print(fruits)
# fruits.append(["Banana", "Guava", "Grapes"])
# print(fruits)


# 4. remove = remove / delete first occurence of certain one element from the list. 
# Syntax: list.remove(item)

# fruits.remove("Mango")
# print(fruits)


# 5. pop = remove / delete certain elemnt from a given index.
# Syntax: list.pop(index)

# fruits.pop(  )
# print(fruits)



# 6. reverse = reverses the list
# Syntax: list.reverse()

# week = ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]
# print(week)
# week.reverse()
# print(week)


# 7. sort = sorts the list in ascending order both alphabetically and numerically
# Syntax: list.sort()

# nums = [4, 9, 0, 1, 2, 8]
# list1 = week + nums
# list1.sort()                             # sort function can sort either only alphabets or numbers not both at the same time.
# print(list1)
# week.sort()
# nums.sort()
# nums.sort(reverse = True)                  # sorts the list in descending order
# print(week)
# print(nums)


# 8. count = counts a particular item / element in the list.
# Syntax: list.count()

# num = [0, 2, 4, 2, 5, 5, 6, 3, 6, 2, 8, 7, 2, 9, 0]
# print(num.count(2))


# 9. Membership Operator

# in = checks if the particular item is present in the list or not.
# not in = oposite of in 

# language = ["python", "java", "c++"]
# print("python" in language)
# print("javascript" not in language)