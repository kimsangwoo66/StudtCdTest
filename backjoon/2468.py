"""
안전영역

알고리즘: bfs

구현아이디어

그래프 입력값중 가장 높은값을
비가 내릴수있는 최대양으로 뽑아서

0부터 최대양까지 반복
bfs 탐색후 안전영역 구하기

반복했을때 안전영역 개수중 최대 값 출력
s
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []

# 올수있는 비의 최대양 선언
maxValue = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    # 지역 그래프 생성
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        # 이지역에 내릴 수 있는 비의 최대양 구하기
        if graph[i][j] > maxValue:
            maxValue = graph[i][j]


def bfs(a, b, water):
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 그래프값이 물의 양보다 키고 방문하지 않았을경우
            if graph[nx][ny] > water and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))


result = 0

# 이지역에 내릴 수 있는 비의 최대 양까지 반복
for i in range(maxValue):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):

            # 내린 비의양이 i일때의 최대 안전영역 개수
            if graph[j][k] > i and visited[j][k] == False:
                bfs(j, k, i)
                cnt += 1

    # 최대값 갱신
    if result < cnt:
        result = cnt

print(result)
