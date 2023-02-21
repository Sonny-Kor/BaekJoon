N = int(input())
arr = list(map(int,input().split(" ")))
arr.sort()

min_arr = []
for i in range(N):
    min_arr.append( arr[i]+arr[(N*2)-1-i])

print(min(min_arr))