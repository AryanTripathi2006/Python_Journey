# Operations on Tuples

# student_detail1 = ("25bcm001", "Jaune")
# student_detail2 = (86.7, 79.5, 91.3, 88.5)

# Concatenation (+)
# student_detail = student_detail1 + student_detail2
# print(student_detail)

# Repetition operator (*)
# t1 = ("class 5", 3000)
# print(t1 * 3)


# Membership operator (in, not in) 
# print(91.3 not in student_detail2)
# print(99.0 not in student_detail2)


# Count = counts the appearance of an element / item in the tuple.
# Syntax: tuple.count(item)
# t1 = 10, 4, 1, 4, 5, 2, 5, 7, 4, 3, 7, 5, 1
# print(t1.count(4))


# index = Returns the index of a first occurence given item in the tuple. It is used in list and strings as well.
# Syntax: tuple.index(item)
# t1 = 10, 2, 1, 4, 5, 2, 5, 7, 4, 3, 7, 5, 1
# print(t1.index(4))
# s1 = "Aryan"
# print(s1.index("a"))
# l1 = [1, 3, 5, 2, 9, 4, 6, 8, 7, 0]
# print(l1.index(2))

# min(), max(), sum()
# Syntax: min(tuple)
# Syntax: max(tuple)
# Syntax: sum(tuple)
# t1 = 10, 2, 1, 4, -5, 2, 5, 0, 7, 4, 3, -7, 5, 1
# print(min(t1))
# print(max(t1))
# print(sum(t1))



# Mutabilty and Immutability

# Mutability = The ability of a value or data to be modified or changed.
# Immutability = Reverse of mutability. Exisisting value will not change instead new value of same data type will be created while usng a function.
# List are mutable whereas tuple and strings are immutable.

# l1 = ["Mango", "Apple", "Banana"]
# print(l1, id(l1))                      # id(x) is used to find the memory adress of variable x.
# l1.append("Guava")
# l1[1] = "Orange"
# print(l1, id(l1))                      # the memory adress of modified list are same therefore list are mutable.

# fruits = ("Mango", "Aple", "Banana")
# print(fruits)
# fruits[1] = "Apple"                    # will give error since tuples are immutable.
# print(fruits)

# s1 = "Python is fun"
# print(s1)
# s1[0] = "p"                            # will give error since strings are also immutable.
# print(s1)