#연구소
#bfs 알고리즘 사용

from collections import deque

#그래프의 세로 및 가로 크기 입력
n, m = map(int, input().split())

#그래프 초기화
graph = []


#그래프 정보 입력
for i in range(n):
    graph.append(list(map(int, input().split())))

newgraph = [[0] * m for _ in range(n)]


dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 0

#바이러스를 퍼트리며 탐색
def bfs():
    global result
    q = deque()

    #새롭게 벽이 생성된 맵 정보 입력
    for i in range(n):
        for j in range(m):
            newgraph[i][j] = graph[i][j]


    #바이러스가 퍼져있는 영역일 경우 큐에 위치 값 추가
    for i in range(n):
        for j in range(m):
            if newgraph[i][j] == 2:
                q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if newgraph[nx][ny] == 0:
                    newgraph[nx][ny] = 2
                    q.append((nx, ny))

    #안전한 영역의 최대값 계산
    result = max(result, scores())

#각 경우의 수별 안전구역 최대값 계산
def scores():
    score = 0
    for i in range(n):
        for j in range(m):
            if newgraph[i][j] == 0:
                score += 1

    return score


def solution(cnt):
    #벽이 3개 만들어졌을 경우
    if cnt == 3:
        bfs()
        return

    # 빈공간에 벽 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt +=1
                solution(cnt)
                #벽 원래대로 복귀
                graph[i][j] = 0
                cnt -=1
solution(0)
print(result)


