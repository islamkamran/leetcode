import heapq

pq = []
heapq.heappush(pq,3)
heapq.heappush(pq,7)
heapq.heappush(pq,-1)
x = heapq.heappop(pq)

print(x)
