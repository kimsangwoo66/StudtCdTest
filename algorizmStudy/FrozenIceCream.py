#음료수 얼려먹기
#bfs 깊이 우선탐색
from collections import deque

n, m = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]


dx = [0,0,-1,1]
dy = [-1,1,0,0]
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                graph[nx][ny] = True
                q.append((nx, ny))








cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            visited[i][j] == True
            bfs(i,j)
            cnt += 1




print(cnt)