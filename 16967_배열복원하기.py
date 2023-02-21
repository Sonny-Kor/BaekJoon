H, W , X , Y = map(int,input().split(" "))

B_Array = []
for i in range(H+X):
    B_Array.append(list(map(int,input().split(" "))))

A_Array = [[-1]*W for _ in range(H)]

for y in range(H):
    for x in range(W):
        if x < Y or y < X:
            A_Array[y][x] = B_Array[y][x]
            continue
        A_Array[y][x] = B_Array[y][x] - A_Array[y-X][x-Y]

for i in range(H):
    print(" ".join([str(each) for each in A_Array[i]]))