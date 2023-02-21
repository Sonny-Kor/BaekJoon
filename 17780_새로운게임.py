import sys
N ,K = map(int,input().split(" "))
round = 0
chessboard = []
chess_map = [[[] for _ in range(N)] for _ in range(N)]
horse = [] # y , x , dir
dx = [1,-1,0,0] # Right Left Up Down
dy = [0,0,-1,1]

for i in range(N):
    chessboard.append(list(map(int,input().split(" "))))
for j in range(K):
    temp = list(map(int,input().split(" ")))
    horse.append(list(map(lambda x:x -1, temp)))
    chess_map[horse[j][0]][horse[j][1]].append(j)



while(round < 1000):
    round += 1
    for i in range(K):
        y, x, dir = horse[i]
        if i != chess_map[y][x][0]:
            continue
        
        nx = x + dx[dir]
        ny = y + dy[dir]

        if not 0 <= nx < N or not 0 <= ny < N or chessboard[ny][nx] == 2: # 파란색 or 밖으로 나간 경우
            if dir == 0 or dir == 1: # 오른쪽, 왼쪽 이동인 경우
                ndir = (dir+1) %2
            else: # 위 아래 이동인 경우 2->3 3->2
                ndir = (dir+1)%2 + 2
            # 한번더 이동
            horse[i][2] = ndir
            nx = x + dx[ndir]
            ny = y + dy[ndir]
            if not 0 <= nx < N or not 0 <= ny < N or chessboard[ny][nx] == 2: # 한번더 밖인경우
                continue 

        chess_set = []
        chess_set.extend(chess_map[y][x])
        chess_map[y][x] = []

        if chessboard[ny][nx] == 1: # 빨간색의 경우
            chess_set.reverse()

        for i in chess_set:
            chess_map[ny][nx].append(i)
            horse[i][:2] = [ny, nx]

        if len(chess_map[ny][nx]) >= 4:
            print(round)
            sys.exit()
        
print(-1)

    



