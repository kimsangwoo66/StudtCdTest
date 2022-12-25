# 연구소
# 알고리즘: BFS

# 구현 아이디어
# 1. 벽을 세울수 있는 모든 조합 반복
# 2. 바이러스 퍼트리기
# 3. 남은 영역 카운팅
# 4. 1,2,3 을 반복해서 남은영역의 최대값 갱신


from collections import deque
from itertools import combinations
import copy


n, m = map(int ,input().split())

#그래프
graph = []

#안전영역 좌표 리스트
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



def bfs(w3graph):
    cnt = 0
    q = deque()

    for ii in range(n):
        for jj in range(m):
            if w3graph[ii][jj] == 2:
                q.append((ii,jj))
                while q:
                    x,y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        #경계값을 넘었을 경우
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        #벽일 경우
                        if w3graph[nx][ny] == 1:
                            continue

                        #안전영역일 경우
                        if w3graph[nx][ny] == 0:
                            #좌표값에 바이러스 넣기
                            w3graph[nx][ny] = 2
                            q.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if w3graph[i][j] == 0:
                cnt += 1

    return cnt



# 그래프에서 안전영역에 3개 벽을만들떄의 모든 조합의 개수만큼 동안 반복
for combi in combinations(safeAreaList, 3):
    #벽을 3개 세우기 위한 그래프 복사
    w3graph = copy.deepcopy(graph)

    #combi 는 3개의 조합된 좌표값들에 벽 넣기
    for c in combi:
        a, b = c
        w3graph[a][b] = 1

    #한 조합의 최종 안전영역 개수
    cnt = bfs(w3graph)

    #조합들 마다 나온 안전영역 개수중 최대값
    result = max(result, cnt)



print(result)

