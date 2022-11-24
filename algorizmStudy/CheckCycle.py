# 사이클 판별 알고리즘
# 그래프에 포함되어있는 간선의 개수가 e개일때
# 모든 간선을 하나씩 확인하며, 매 간선 e에 대하여 union 및 find 함수를 호출하는 방식으로 동작

#특정원소가 속한 집합 찾기
def find_parent(parent, a):
    #루트 노드가 아니라면 루트 노드를 찾을때 까지 호출
    if parent[a] != a:
        return find_parent(parent, parent[a])

    return a

#두 원소가 속한 집합 합치기

def union_parent(parent, a, b):

    #두 원소가 속한 집합 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b

    else:
        parent[b] = a

#노드의 개수 v와 간선의 개수 e 입력받기
v, e = map(int, input().split())

#부모테이블 초기화
parent = [0] * (v+1)


#부모테이블을 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#사이클 발생여부
cycle = False

#간선 개수만큼 반복
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break

    #사이클이 발생하지 않았더라면 합집합 수행
    else:
        union_parent(parent, a, b)


if cycle:
    print("사이클 발생")

else:
    print("사이클 발생안함")


