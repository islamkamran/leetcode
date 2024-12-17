from queue import Queue
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q)
x = q.pop()  # Removes and returns 1
print(x)
