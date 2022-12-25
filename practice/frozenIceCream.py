# 음료수 얼려먹기
# 사용알고리즘 : bfs

# bfs로 탐색을하다가
# 안가본 곳이라면 전부 1로 변경 후 개수 카운트 + 1

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

cnt = 0

dx = [0, 1, 0, -1]  # 아래 , 위 이동

dy = [1, 0, -1, 0]  # 오른쪽 왼쪾 이동


def bfs(x, y):
    q = deque()
    q.append((x, y))

    result = False
    while q:
        # 탐색 시작 좌표를 꺼냄
        x, y = q.popleft()

        # 현재좌표 방문 처리
        graph[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #nx >=n or ny >=m 에서 = 로 한이유는 실제로 좌표가 0,0 ~ 4,4까지 만들어지기 때문
            #ex) n = 5 , m=5 일경우 실제 만들어지는 좌료의 마지막은 4,4
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))

                result = True

    return result


for i in range(n):
    for j in range(m):
        if bfs(i, j):
            cnt += 1

print(cnt)
