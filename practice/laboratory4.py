# 연구소

# 알고리즘: bfs + 백트래킹


# 구현아이디어
# 1.모든 조합의 경우의 수를 탐색해야함 -> 백트래킹 사용
# 2.해당 조합의 그래프를 사용해 바이러스를 퍼트림
# 3.조합으로 나온 안전영역중 가장 큰값을 반환
from collections import deque
import copy

n, m = map(int, input().split())

graph = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))


def virus():
    cnt = 0
    q = deque()
    newgraph = copy.deepcopy(graph)
    for ii in range(n):
        for jj in range(m):
            if newgraph[ii][jj] == 2:
                q.append((ii, jj))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if newgraph[nx][ny] == 0:
                newgraph[nx][ny] = 2
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if newgraph[i][j] == 0:
                cnt += 1

    return cnt


result = 0


def backtrack(cnt):
    global result
    # 벽이 3개 세워졌을경우
    if cnt == 3:
        value = virus()
        result = max(result, value)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                backtrack(cnt + 1)

                graph[i][j] = 0

backtrack(0)

print(result)
