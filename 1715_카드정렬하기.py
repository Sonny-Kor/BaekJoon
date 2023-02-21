#https://www.acmicpc.net/problem/1715
#카드정렬하기
import heapq

T = int(input())
heap = []
for i in range(T):
    heapq.heappush(heap,int(input()))
if T == 1:
    print(0)
else:
    result = 0
    for i in range(T):
        if(len(heap) == 0 or len(heap) == 1):
            break
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        result += (min1 + min2)
        heap.append(min1+min2)
    print(result)
