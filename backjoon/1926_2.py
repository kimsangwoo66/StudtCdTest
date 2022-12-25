# 백준 1926

from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0


def bfs(x, y):
    rs = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:

        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]

            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    rs += 1
                    q.append((nx, ny))
    return rs


cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            result = max(result, bfs(i, j))

print(cnt)
print(result)
