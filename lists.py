# list in python which are vectors in C++

vector1 = [1,2,3,4,5]
vector2 = [5,6,7,8]

# vector[1] = 10
# vector.append(12)
# vector.extend([1,2,3,4])
# vector.insert(1,33)
# vector.remove(2)
# # x = vector.pop(1)
# # print(x)
# del vector[2]
# # del vector[:]
# vector.clear()
# print(vector)

# enumerate
# for index,value in enumerate(vector):
#     print(index,value)
# vector.sort()
# vector = sorted(vector)
# vector.reverse()
# vector = vector[::-1]
# ind = vector.index(1)
# print(ind)
# print(vector.count(1))
# sub_vec = vector1[0:2]
# print(sub_vec)
# print(vector1)
# print((vector1+vector2)*2)
all_positive = all(x<0 for x in vector1)
print(all_positive)
any_odd = any(x%2!=0 for x in vector2)
print(any_odd)

nested = [[[1,2], [2,4]]]

flatten = [item for sublist in nested for subsublist in sublist for item in subsublist]
print(flatten)