#음료수 얼려먹기
#연결 요소 찾기

#DFS 활용

#간단한 알고리즘 원리
#1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점중에서 값이 0이면서 아직 방문하지 않은 지점이라면 방문 처리
#2. 방문 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면 , 연결된 모든 지점을 방문 가능
#3. 1~2 번을 반복하며 방문하지 않은 지점의 수를 더하고 리턴


# 후기
# 답보고 해결함
# 어떻게 접근해야 할지는 알았는데
# dfs 코드를 어떻게 짜야될지 너무 오래 고민
# 탐색하다가 1이 나오면 탈출하는 방식으로 생각하다가 구현 못함
# true, false를 어떻게 적절히 활용해야할지 파악 못함



def dfs(x, y):
    if x <= -1 or y <= -1 or x >= N or y >=M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False

#세로 길이 N , 가로 길이 M
N, M = map(int ,input().split())

#2차원 리스트 맵정보 입력
graph = []
for i in range(N):
    graph += [list(map(int, input()))]

#만들 수있는 아이스크림 개수
cnt = 0
#모든 지점을 탐색
for i in range(1, N+1):
    for j in range(1, M+1):

        #현재 위치에서 dfs 수행
        if dfs(i,j) == True:
            cnt +=1

print(cnt)