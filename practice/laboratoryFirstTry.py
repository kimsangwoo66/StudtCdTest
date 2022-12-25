# 연구소
# 알고리즘: BFS

# 구현 아이디어
# 1. 벽세우기 ->  연구소 좌표의 모든 안전공간에 3개씩 벽을 세울 수 있는 모든 조합을 탐색
# 2. 바이러스 퍼트리기
# 3. 남은 영역 카운팅


from collections import deque
from itertools import combinations
import copy


n, m = map(int ,input().split())

graph = []
safeAreaList = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 0

for i in range(n):
    graph.append(list(map(int, input().split())))



#안전영역 리스트 좌표 삽입
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            safeAreaList.append((i, j))



def bfs(graph, x, y):
    cnt = 0
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #경계값을 넘었을 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                continue

            # if graph[nx][ny] == 0:
            #     graph[nx][ny] = 2
            #     q.append((nx,ny))
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx,ny))





# 그래프에서 안전영역에 3개 벽을만들떄의 모든 조합의 개수만큼 동안 반복
for combi in combinations(safeAreaList, 3):
    cnt = 0
    #벽을 3개 세우기 위한 그래프 복사
    w3graph = copy.deepcopy(graph)
    #combi 는 3개의 좌표가 1 이어야함
    for c in combi:
        a, b = c
        w3graph[a][b] = 1

    bfs(w3graph)


    for i in range(n):
        for j in range(m):
            if w3graph[i][j] == 0:
                cnt += 1

    result = max(result, cnt)





print(result)

