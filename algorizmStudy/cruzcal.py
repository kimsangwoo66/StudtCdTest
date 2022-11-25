#크루즈칼 알고리즘

#최소신장트리에 해당되는 노드들의 간선의 총합을 길이를 더해 반환한다.

#크루스칼 알고리즘은 간선의 개수가 E개일때 ElogE의 시간복잡도를 갖는다.
def find_parent(parent, a):

    #루트노드를 찾아서 반환
    if parent[a] != a:
        return find_parent(parent, parent[a])

    return a

#두 원소가 속한 집합을 합치기
def union_find(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


#노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())

#부모테이블 초기화
parent = [0] * (v+1)

#부모테이블의 루트노드를 자기 자신으로 변경
for i in range(1, v+1):
    parent[i] = i

#모든 간선에 대한 정보를 담을 리스트 선언
edges = []
#비용에 대한 총합을 담을 변수
result = 0

#간선에 대한 정보 입력
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))


#간선을 비용순으로 정렬
edges.sort()

#간선을 하나씩 확인
for edge in edges:

    cost, a, b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_find(parent, a, b)
        result += cost

print(result)






