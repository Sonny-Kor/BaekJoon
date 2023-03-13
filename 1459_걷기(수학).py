X, Y, W, S = map(int,input().split(" ")) # W = 직선이동  S = 대각이동

my_x , my_y = 0, 0

case1 = (X+Y) * W # 직선만으로 갔을때 비용
case2 = 0 # 대각으로 만 간 비용
case3 = 0 # 대각최대한 + 직선
if (X+Y)%2 == 0:
    case2 = max(X,Y)*S
else:
    case3 = (max(X,Y)-1)*S+W
case4 = min(X,Y)*S + W*abs(X-Y) #대각 최소 직선최대

arr = [case1,case2,case3,case4]

for i in arr:
    if i == 0:
        arr.remove(i)
print(min(arr))