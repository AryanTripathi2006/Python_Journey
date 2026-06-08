# Tuple = sequence of items as a collection enclosed within ()
# (item1, item2, item3, ....)
# ordered, immutable, Duplicacy allowed

t1 = ("Python", 10, 20.0, True, None, [1,2,3], (10, 20))
t2 = 10, 20, 30 ,40                                        # not neccessary to put () for tuple.
# print(len(t1))
# print(t2)
# print(type(t2))

# Acessing item / element in a tuple.
# print(t1[0])
# print(t1[-1])
# print(t1[-4:])

# Typecasting

# l1 = [1, 2, 3]
# print(l1, type(l1))
# t3 = tuple(l1)
# print(t3, type(t3))

l2 = list(t1)
print(l2, type(l2)) 