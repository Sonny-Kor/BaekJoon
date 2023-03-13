def pr(arr):

    for i in range(R):
        for j in range(C):
            print('{}'.format(arr[i][j]), end='')
        print()

R, C, N = map(int,input().split(" "))

arr = []
for i in range(R):
    arr.append(input())

all_boom = [['O']*C for _ in range(R)]
first_boom = [['O']*C for _ in range(R)]
second_boom = [['O']*C for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O': # 처음 폭탄의 위치만 터져야함
            first_boom[i][j] = '.'
            for k in range(4): # 상우하좌
                x = i + dr[k]
                y = j + dc[k]
                if -1 < x < R and -1 < y < C:
                    first_boom[x][y] = '.' # 터진걸로 체크

for i in range(R):
    for j in range(C):
        if first_boom[i][j] == 'O': # 처음 폭탄의 위치만 터져야함
            second_boom[i][j] = '.'
            for k in range(4): # 상우하좌
                x = i + dr[k]
                y = j + dc[k]
                if -1 < x < R and -1 < y < C:
                    second_boom[x][y] = '.' # 터진걸로 체크

if N <= 1:
    pr(arr)
elif N % 2 == 0:
    pr(all_boom)
elif N>1 and N % 4 == 1:
    pr(second_boom)
elif N>1 and N % 4 == 3:
    pr(first_boom)