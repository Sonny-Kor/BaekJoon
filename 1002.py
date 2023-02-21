# https://www.acmicpc.net/problem/1002
import math
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split(' '))

    # 터렛 간의 거리
    
    distance = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
    # 원의 중심이 같은 경우
    if (distance == 0):
        # 두 원이 일치하는 경우
        if (r1 == r2):
            print(-1)
        else:
            print(0)
    # 원의 중심이 다른 경우
    else:
        if abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
            print(2)
        elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
            print(1)
        else:
            print(0)