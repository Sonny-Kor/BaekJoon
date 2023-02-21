from collections import deque
N , M = map(int,input().split(" "))

bitmap = []
visited = [ [0] * M for _ in range(N)]
for i in range(N):
    bitmap.append(list(map(int,input().split(" "))))

def bfs():
    graph = deque([0,0])
    visited[0][0] = True
    while(graph):
        y = graph.popleft()
        x = graph.popleft()
    

bfs()