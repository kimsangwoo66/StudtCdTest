from collections import deque
n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


visited = [[False] * n for _ in range(n)]

dx = [0,1,0,-1] # 위 어래
dy = [1,0,-1,0] # 왼쪽 오른쪽
blockList = []

def bfs(a,b):
    cnt = 1
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt


cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            b = bfs(i,j)
            blockList.append(b)
            cnt += 1

blockList.sort()

print(cnt)

for block in blockList:
    print(block)











