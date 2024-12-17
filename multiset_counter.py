# multiset is treated as counter in python but we have to import a library for it

from collections import Counter
unordered_multiset = Counter([1,1,2,3,4,3,3])
print(unordered_multiset)

unordered_multiset[2]+=7
print(unordered_multiset)

unordered_multiset[2]-=2
print(unordered_multiset)
# the one with highest priority comes on the first position.

# empty_counter = Counter({1:3,2:1,4:2})
# print(empty_counter)
del unordered_multiset[2]
print(unordered_multiset)

unordered_multiset.update([1,4,3,3])
print(unordered_multiset)
c1 = Counter([1,2])
c2 = Counter([1,1,1,1])
# negative values in the subs are ignored
print(c1|c2)

for key,count in unordered_multiset.items():
    print(key,"=",count)

list_elem = list(unordered_multiset.elements())
print(list_elem)
print(unordered_multiset.clear())