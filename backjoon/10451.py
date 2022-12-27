"""
순열사이클

알고리즘: 재귀, dfs

구현 아이디어

해당 번째의 1번쨰 인덱스 값 -> (1번쨰 인덱스 값)의 인덱스 값 -> ....-> 마지막 인덱스값이 첫번째 인덱스값일 경우 (사이클 발생) 카운트

"""

import sys

# 파이썬 기본 재귀 1000 따라서 100000으로 변경
sys.setrecursionlimit(10000)
input = sys.stdin.readline

t = int(input())


def dfs(v):
    # 방문처리
    visited[v] = True

    # 탐색 리스트에 추가
    chase.append(v)

    # 다음 방문해야하는 인덱스 값
    nextF = tlist[v]

    # 다음 방문해야하는 인덱스 값이 이미 방문처리 됬고 and 다음 방문해야하는 인덱스 값이 이미 탐색됬었다면 (사이클이 성립됬다면)
    if visited[nextF] and nextF in chase:

        tcycle.append((chase[chase.index(nextF):]))
        return

    else:
        dfs(nextF)

#테스트 케이스별 사이클 개수를 담을 리스트 선언
result = []

for _ in range(t):
    n = int(input())
    #튜플 형태의 사이클 집합 형태를 담을 리스트 선언
    tcycle = []
    tlist = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            #탐색 리스트 선언
            chase = []

            #dfs 처리
            dfs(i)

    result.append(len(tcycle))

for end in result:
    print(end)
