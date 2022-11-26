#dfs 깊이 우선 탐색

#각 노드가 연결된 정보 표현 , 무방향 그래프
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#현재 노드를 방문 처리
visited = [False] * 9


def dfs(graph, v, visited):
    #해당 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    #현재 노드와 인접한 노드 탐색
    for i in graph[v]:
        #현재 노드와 인접한 노드를 방문하지 않은 상태라면
        if not visited[i]:
            #재귀함수 호출
            dfs(graph, i, visited)

#노드 번호가 작은 노드부터 탐색 시작
result = dfs(graph, 1, visited)

print(result)