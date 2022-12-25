#dfs
#깊이 우선탐색
#중요한점, 재귀, 인접노드리스트(0번째 행은 비워둠, 방문여부 리스트)

#인접노드 그래프 리스트, 시작, 방문여부
def dfs(graph, v, visited):
    #방문여부를 승인처리
    visited[v] = True

    #현재 노드와 연결된 다른노드를 재귀적으로 방문
    for i in graph[v]:
        #방문하지 않았다면
        if visited[i] == False:


            return dfs(graph, i, visited)

