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
 
result = 0
def dfs(x,y,count):
    global result
    if ( miro[y][x] == 0):
        return
    if y == N-1 and x == M-1:
        if result == 0 or result > count:
            result = count

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if (next_x < 0 or next_x >=M or  next_y < 0 or next_y >= N):
            continue
        if (visited[next_y][next_x] == 0):
            visited[next_y][next_x] = 1
            dfs(next_x,next_y,count+1)
            visited[next_y][next_x] = 0
    
dfs(0,0,1)
print(result)