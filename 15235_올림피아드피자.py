N = int(input())
arr = list(map(int,(input().split(" "))))

count = 0
def allzero(arr):
    temp = 0
    for i in arr:
        if i >= 0:
            return True
    return False

result = [0] * N
while(allzero(arr)):
    for idx, pizza in enumerate(arr):
        if pizza > 0:
            count += 1
        arr[idx] -= 1
        if arr[idx] == 0:
            result[idx] = count
    
for i in result:
    print(i,end=" ")


