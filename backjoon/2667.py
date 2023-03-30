"""
단지 번호 붙이기

구현 아이디어:
bfs
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))



visited = [[False] * n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]




def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                graph[nx][ny] = 0
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            value = bfs(i, j)
            result.append(value)

print(len(result))
result.sort()
for i in result:
    print(i)