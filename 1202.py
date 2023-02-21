import heapq
import sys

heap = []
bag_weight = []
N, K = map(int,sys.stdin.readline().split(' '))
for i in range(N):
    relic = list(map(int,sys.stdin.readline().split(' ')))
    relic[0],relic[1] = -1 * relic[1],relic[0]
    
    heapq.heappush(heap,relic)

for i in range(K):
    heapq.heappush(bag_weight,int(input()))

result = 0
# for i in range(N):
#     max = heapq.heappop(heap)
#     for bag in bag_weight:
#         if (max[1]) <= bag:
#             result += -1 * max[0]
#             bag_weight.remove(bag)
#             break

for i in range(K):
    max = heapq.heappop(heap)

    bag = heapq.heappop(bag_weight)
    if(max[1]) <= bag:
        result += -1 * max[0]
    else:

        heapq.heappush(bag_weight,bag)


print(result)