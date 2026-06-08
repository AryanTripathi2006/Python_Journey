# Operations on set

nums1 = {1, 2, 3, 0, 5}
nums2 = {4, 6, 9}

# Membership Operators(in, not in)
# print(0 in nums)
# print(10 not in nums)

# Concatenation?
# print(nums1 + nums2)              # Concatenation not allowed in sets.

# Repeating sets?
# print(nums1 * 3)                  # Repetiyion not allowed in sets.

# Typecasting
# weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
# weekdays = set(weekdays)
# print(weekdays)

# Are sets mutable or immutable?
# Sets are mutable

#add()
# Syntax: set.add(item)
# nums1.add(17)
# print(nums1)

# remove()
# Syntax: set.remove(item)
# nums1.remove(5)
# print(nums1)

# discard()                     # The difference between remove and discard is dicard do not give error if some element is not present in the set wheres remove gives error
# Syntax: set.discard(item)
# nums1.discard(10)
# print(nums1)

student1 = {"English", "Math", "CS", "Physics", "Chemistry"}
student2 = {"English", "Biology", "Physics", "Chemistry"}
student3 = {"English", "Sanskrit", "Math", "CS"}

# print(student1 , type(student1))
# print(student2 , type(student2))

# common subjects of student1 and student2 : Intersection
# common_sub = student1.intersection(student2, student3)
# common_sub = student1 & student2 & student3
# print(common_sub)

# all subjects of student1 and student2 : union
# all_sub = student1.union(student2, student3)
# all_sub = student1 | student2 | student3
# print(all_sub)


days = {"Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"}
week_ends = {"Sat", "Sun"}

# difference of set
# week_days = days - week_ends         # elements of days which are not in weekends.
# week_days = days.difference(week_ends)
# print(week_days)


# Frozen Sets - Immutable Sets
fs1 = frozenset({10, 20, 30})
# print(fs1, type(fs1))
# fs1.add(40)                       # error since frozensets are immutable
# print(fs1)

fs2 = frozenset({0, 40, 10, 20})
print(fs1 & fs2)
print(fs1 | fs2)
print(fs1 - fs2)
print(fs2 - fs1)