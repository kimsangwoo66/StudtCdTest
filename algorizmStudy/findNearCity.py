#특정 거리의 도시 찾기
#모든 간선의 길이가 같고 최단거리를 구하는 문제일 경우 BFS 사용
from collections import deque
#도시의 개수N , 도로의개수 M, 거리정보 K ,출발 도시의 번호 X
N,M,K,X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
   a, b = map(int,input().split())
   graph[a].append(b)

#모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)

#출발 도시에 대한 거리 설정
distance[X] = 0


q = deque()
q.append(X)

while q:
    v = q.popleft()
    #print(v, end=' ')

    for i in graph[v]:
        #아직 한번도 방문하지 않은 노드라면
        if distance[i] == -1:
            distance[i] = distance[v] + 1
            q.append(i)

#최단 거리가 K인 모든 도시의 번호를 오름차순으로 정렬
check = False

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)








