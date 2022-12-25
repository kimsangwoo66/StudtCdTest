#특정거리의 도시 찾기
#bfs
from collections import deque


#도시의 개수: N, 도로의 개수: M, 거리정보: k, 출발도시의 번호: X

n,m,k,x = map(int, input().split())


#모든 노드에 대한 최단거리리스트 테이블 초기화
distance = [0] * (n+1)
#그래프 초기화
graph = [[] for _ in range(n+1)]

for i in range(m):

    #인접한 노드 정렬
    a, b = map(int, input().split())
    graph[a].append(b)


q = deque()

#시작
q.append(x)

#시작 최단거리 리스트 갱신
distance[x] = 0

while q:
    v = q.popleft()
    for i in graph[v]:
        if distance[i] == 0:
            distance[i] = distance[v] + 1
            q.append(i)


for i in range(1, n+1):
    if distance[i] == k:
        print(i)



if k not in distance:
    print("-1")


