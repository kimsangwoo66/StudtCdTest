import sys
from collections import deque

input = sys.stdin.readline


#m은 상자의 가로 칸의 수, n은 상자의 세로 칸의 수
m, n = map(int, input().split())

graph = []

#방문 여부
visited = [[False] * (m+1) for _ in range(n+1)]


# 좌 우
dy = [0,-1,0,1]
# 상 하
dx = [1,0,-1,0]
q = deque()


for i in range(n):
    graph.append(list(map(int, input().split())))

# 익은 토마토 큐에 넣기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))



def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                #익히고 1을 더함
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                visited[nx][ny] = True


result = 0

bfs()
for i in graph:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    result = max(result, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(result - 1)







