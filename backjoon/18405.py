#경쟁적 전염
# 1초 동안 기존에 시험관에 존재하는 세균들이 번호가 작은 순으로 증식
# bfs로 풀기
#
from collections import deque

n, k = map(int , input().split())

##초기 시험관에 있는 바이러스 리스트
graph = []

##초기 시험관에 있는 바이러스 정보 리스트
data = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    #초기 시험관에 있는 바이러스 입력
    graph.append(list(map(int, input().split())))

#S초뒤에 알고싶은 좌표값 입력
S, X, Y = map(int, input().split())

for i in range(n):
    for j in range(n):
        #초기 시험관에 있는 바이러스 정보 입력 , 비아러스번호, 퍼진 시간, 위치
        data.append((graph[i][j], 0, i, j))


#세균 번호가 작은값부터 정렬
data.sort()
q = deque(data)

#bfs 시작
while q:
    #바이러스, 시간, 위치
    virus, cnt, x, y = q.popleft()
    #입력한 S초가 지났으면 탈출
    if cnt == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >=0 and nx < n and ny < n:
            if graph[nx][ny] == 0:
                #안전영역에 바이러스 삽입
                graph[nx][ny] = virus

                #큐에 기존에 시간을 증가시켜 추가
                q.append((virus, cnt+1, nx, ny))


print(graph[X-1][Y-1])









