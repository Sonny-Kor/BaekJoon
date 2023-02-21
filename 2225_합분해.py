import math
N = input()

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in N:
    i = int(i)
    arr[i-1] += 1

temp = math.ceil((arr[5] +arr[8])/2)
arr[5] = temp
arr[8] = temp

print(max(arr))