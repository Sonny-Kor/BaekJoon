

while(True):
    arr = list(map(int,input().split(" ")))
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    arr.sort(reverse= True)
    if arr[0] >= arr[1] + arr[2]:
        print("Invalid")
    else:
        if arr[0] == arr[1] == arr[2] :
            print("Equilateral")
        else:
            temp = set(arr)
            temp1 = list(temp)
            if len(temp1) == 2:
                print("Isosceles")
            elif len(temp1) == 3:
                print("Scalene")