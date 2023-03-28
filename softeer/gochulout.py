import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())



graph = [[] for _ in range(n + 1)]

graphReverse = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    # 노드별 인접 노드 저장 리스트
    graph[a].append(b)
    graphReverse[b].append(a)

# 출발지, 목적지 입력
s,t = map(int, input().split())


def dfs(now, graph, visited):
    if visited[now] == 1:
        return
    visited[now] = 1
    for neighbor in graph[now]:
        dfs(neighbor, graph, visited)
    return

fromS = [0] * (n + 1)
# 출근길에서 t를 만났을 경우 따라가지 않음
fromS[t] = 1
dfs(s, graph, fromS)

fromT = [0] * (n + 1)
# 퇴근길에서 s를 만났을 경우 따라가지 않음
fromT[s] = 1
dfs(t, graph, fromT)

toS = [0] * (n + 1)
dfs(s, graphReverse, toS)

toT = [0] * (n + 1)
dfs(t, graphReverse, toT)

count = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toT[i] and toS[i]:
        print("체크: ",fromS[i] and fromT[i] and toT[i] and toS[i])
        count += 1
#출발점과 끝점까지 모두 카운트 하기 때문에 - 2
print(count - 2)

print("graph: ", graph)
print("graphReverse: ", graphReverse)

print("fromS: ", fromS)
print("fromT: ", fromT)
print("toS: ", toS)
print("toT: ", toT)


