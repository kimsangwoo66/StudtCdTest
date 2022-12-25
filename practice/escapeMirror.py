#이코테 미로탈출
#사용 알고리즘 : bfs


from collections import deque

# n x m 사이즈의 미로
n, m = map(int, input().split())

graph = []


for i in range(n):
    # (0,0) 부터 (n-1,m-1) 까지의 좌표 생성
    graph.append(list(map(int, input())))

dx = [0,1,0,-1] # 아래, 위 이동
dy = [1,0,-1,0] # 오른쪽, 왼쪽 이동


def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            #벽 일경우 건너뜀
            if graph[nx][ny] == 0:
                continue

            #좌표를 처음 방문하는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


bfs(0,0)

#bfs를 사용한 결과
# 그래프의 가장 오른쪽 아래까지의 최단거리 값
print(graph[n-1][m-1])

