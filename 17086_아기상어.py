from collections import deque
N, M = map(int, input().split(" "))

array = []
visited = [[0]* M for _ in range(N)]
q = deque()
maxDistance = 0
for _ in range(N):
    array.append(list(map(int,input().split(" "))))


def bfs():
    global maxDistance
    while q:
        y = q.popleft()
        x = q.popleft()

        dy = [-1,-1,-1,0,0,1,1,1 ]
        dx = [-1,0,1,-1,1,-1,0,1 ]
        for i in range(8):
            move_y = y + dy[i] 
            move_x = x + dx[i]

            if (move_y < 0 or move_x < 0 or move_y >=N or move_x >= M):
                continue
            if (visited[move_y][move_x] == 0):
                visited[move_y][move_x] = 1
                array[move_y][move_x] = array[y][x] + 1
                maxDistance = maxDistance if maxDistance > array[move_y][move_x]  else array[move_y][move_x]
                q.append(move_y)
                q.append(move_x)

for i in range(N):
    for j in range(M):
        if array[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            q.append(i)
            q.append(j)
bfs()
print(maxDistance-1)