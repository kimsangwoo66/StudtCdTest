# 특정 거리의 도시 찾기

# 사용 알고리즘: bfs

# 구현 아이디어

# 모든 간선의 길이가 같고, 단방향 이기떄문때 bfs 사용
# 인접 리스트 그래프 사용
# 시작 도시에서 각 도시의 최단거리 값을 담을 리스트 사용

from collections import deque

n, m, k, x = map(int, input().split())

# 각도시의 인접 도시를 나타낼 리스트 선언
graph = [[] for _ in range(n + 1)]

INF = int(1e9)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

Ldistance = [INF] * (n + 1)
Ldistance[x] = 0


def bfs(x):
    q = deque()
    q.append(x)

    while q:
        v = q.popleft()

        for i in graph[v]:
            if Ldistance[i] == INF:
                Ldistance[i] = Ldistance[v] + 1
                q.append(i)


bfs(x)

for i in range(len(Ldistance)):
    if Ldistance[i] == k:
        print(i)

if k not in Ldistance:
    print(-1)

# 출발 도시 x에서 x로 가는 최단거리 0
