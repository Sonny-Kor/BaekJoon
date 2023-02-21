import sys

input=sys.stdin.readline
T =int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int,input().split(" ")))
    buy_index = []
    mymoney = 0
    count = 0
    # 아무것도 안한다 -> 자기보다 작은 숫자가 뒤에 나오면
    # sell_price = [0 for _ in range(N)]
    
    for i in range(N-1):
        if price[i] <= price[i+1]: # 산다
            buy_index.append(i)
            mymoney -=  price[i]

    for i in range(N):
        for j in range(i,-1,-1):
        
            if price[i] >= price[j]:
                price[j] = price[i]
    for i in buy_index:
        mymoney += price[i]

    print(mymoney)