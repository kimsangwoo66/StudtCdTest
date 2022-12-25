#BFS
#너비 우선 탐색
#가까운 노드부터 우선적으로 탐색하는 알고리즘
#큐 자료구조 이용

#기본
#탐색 시작 노드를 큐에 삽입 -> 해당 노드 방문처리
#큐에서 해당 노드 빼기 -> 해당 노드와 인접한 모든 노드중 작은 번호의 노드부터 큐에 삽입 -> 해당 노드들을 전부 방문처리
#더 이상 2번의 과정을 수행할 수 없을 때까지 반복

#간선의 길이가 동일한 값에서 최단거리 문제를 해결하기 위한 목적으로 사용

from collections import deque

def bfs(graph, start, visited):
    visited[start] = True
    q = deque()
    while q:
        v = q.popleft()

        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:

            if not visited[i]:
                visited[i] = True
                q.append(i)






