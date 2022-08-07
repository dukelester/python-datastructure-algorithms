import heapq


H = [21,1,45,78,3,5]

heapq.heapify(H)
print(H)

heapq.heappush(H, 300)
print(H)
heapq.heapify(H)
heapq.heappop(H)

heapq.heapreplace(H, 5)
print(H)
