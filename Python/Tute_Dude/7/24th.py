# Shallow Copy or Deep Copy
# This is a concept for mutable data-types

import copy

l1 = [1, 2.5, [10, 20, 30], 'python']

# Shallow copy: In this the memory location of all the inner elements remains when copied.
l2 = copy.copy(l1)
# print(l2)
# print(id(l1), id(l2))
# l1[0] = 100                                # After updating the memory location of l1[0] gets changes since ut gets reassigned
# l1[2][0] = 50                              # But here the memory of inner list does not get changed. Therefore after reassiging the updated value gets reflected in both l1 & l2.
# print(f"l1 -> {l1} {id(l1)}")
# print(f"l2 -> {l2} {id(l2)}")
# print(id(l1[0]), id(l1[2]))
# print(id(l2[0]), id(l2[2]))


# Deep copy: In this the memory location of all the inner elements gets changed when copied.
l2 = copy.deepcopy(l1)
l1[0] = 100
l1[2][0] = 50
print(f"l1 -> {l1} {id(l1)}")
print(f"l2 -> {l2} {id(l2)}")
print(id(l1[0]), id(l1[2]))
print(id(l2[0]), id(l2[2]))