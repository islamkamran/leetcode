# Un ordered sets in C++ are sets in python implemened through hashmap

# unordered_set = {1,2,3,5,7,8,9}
# unordered_set.add(4)
# unordered_set.remove(2)
# unordered_set.discard(9)
# elem = unordered_set.pop()
# print(unordered_set)
# unordered_set.clear()
# print(elem)
# print(unordered_set)

# sets operations

set1={1,2,6}
set2={4,5,3}
print(set1)
print(set2)
# print(set1 | set2)
# print(set1-set2)
# print(set1 ^ set2)
print(set1>=set2)
print(set1.isdisjoint(set2))

for e in set1:
    print(e)

tuple_s = tuple(set1)
print(tuple_s)

new_s = set1.copy()
print(new_s)
print(len(set1))