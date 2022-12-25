from collections import deque
import copy

n, m = map(int, input().split())

graph = []

visited = [[False] * m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]


for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(a,b):
    cnt = 1
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                graph[nx][ny] = 0
                visited[nx][ny] = True
                cnt += 1
                q.append((nx,ny))

    return cnt


cnt = 0
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            result = max(result, bfs(i,j))
            cnt += 1

print(cnt)
print(result)


