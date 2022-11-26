# bfs 넓이 우선탐색
# 그래프에서 가까운 노드 부터 우선적으로 탐색
# bfs는 큐 자료구조를 이용 , ex) deque

# 간단한 알고리즘 원리
# 1. 탐색 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 2번의 과정을 수행할 수없을 떄까지 반복

# dfs 와 다른점은 bfs는 인접노드들을 한번에 큐에 넣고 처리함
#간선의 길이가 모두 동일한 상황에서 최단거리를 구하는 목적으로도 많이 사용

from collections import deque

#각 노드가 연결된 정보 표현 , 무방향 그래프 (2차원 리스트)
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

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

#탐색 기준: 번호가 낮은 노드부터

def bfs(graph, v, visited):

    #큐 구현을 위해 덱 라이브러리 사용
    q = deque()

    #큐에 시작 노드 삽입
    q.append(v)

    while q:
        #큐에서 하나의 원소를 뽑기
        v = q.popleft()

        #해당 노드 방문 처리
        visited[v] = True
        print(v, end=' ')

        #방문한 노드와 인접한 노드 탐색
        for i in graph[v]:
            # 방문 상태의 노드와 인접한 노드가 아직 방문처리가 되지 않았다면
            if not visited[i]:
                #해당 노드 방문처리
                visited[i] = True

                #큐에 인접노드 추가
                q.append(i)


result = bfs(graph, 1, visited)

print(result)




