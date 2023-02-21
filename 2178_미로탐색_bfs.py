from collections import deque

N, M = map(int,input().split(" "))
miro = []
visited = []
for y in range(N):
    col = input()
    col2 = []
    visited2 = []
    for x in col:
        col2.append(int(x))
        visited2.append(0)
    miro.append(col2)
    visited.append(visited2)
def bfs():
    queue = deque([0,0])

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        if y == N-1 and x == M-1:
            break
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if (next_x < 0 or next_x >=M or  next_y < 0 or next_y >= N):
                continue
            if visited[next_y][next_x] == 0 and miro[next_y][next_x] == 1:
                queue.append(next_x)
                queue.append(next_y)
                visited[next_y][next_x] = visited[y][x] + 1
    print(visited[N-1][M-1]+1)
bfs()