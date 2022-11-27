#백준 1926 그림
#bfs 알고리즘
from collections import deque
#세로 n 가로 m
n,m = map(int, input().split())

#맵 리스트 생성
graph = []
#방문 테이블
visited = [[False] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x, y):
    rs = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:

        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >=m:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))
                rs += 1

    return rs





cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            cnt += 1
            max_size = max(max_size, bfs(i,j))


print(cnt)
print(max_size)

