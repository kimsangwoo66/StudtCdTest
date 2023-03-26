"""
줄세우기

알고리즘: 위상정렬

조건

학생 A는 학생 B앞에 서야함
"""

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

# 진입차수 테이블 초기화
indgree = [0] * (n+1)

# 정점과 인접한 정점들의 정보를 저장하는 리스트 초기화
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

    indgree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1,m+1):

        # 진입 차수가 0인 노드들을 전부 큐에 삽입
        if indgree[i] == 0:
            q.append(i)

    while q:

        # 큐에 있는 노드를 꺼냄
        now = q.popleft()

        # 결과 리스트에 삽입
        result.append(now)

        #현재 노드에 인접한 노드를 탐색
        for i in graph[now]:

            # 방문하지 완료되지 않은 노드들의 진입 차수 1 감소
            indgree[i] -= 1

            # 진입 차수가 0으로된 노드를 q에 삽입 = 방문 완료 처리
            if indgree[i] == 0:
                q.append(i)

    for j in result:
        print(j, end=" ")


topology_sort()