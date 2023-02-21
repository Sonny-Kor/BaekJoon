import heapq

heap = []

heapq.heappush(heap,3)
heapq.heappush(heap,4)
heapq.heappush(heap,5)
heapq.heappush(heap,6)
heapq.heappush(heap,1)

print(heapq.heappop(heap))