#특정 노드가 속한 집합 찾기
def find_parent(parent, a):
    if parent[a] != a:
        return find_parent(parent, parent[a])
    return a


#두 원소가 속한 집합을 합치기 ex) a가 3, b가 2  그럼 3에 p[3] = 3 p[2] = 2
def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b

    else:
        parent[b] = a



#노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())

#부모 테이블 초기화 하기
parent = [0] * (v+1)

#부모테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i


#union 연산을 노드 2개씩 실행
#간선의 개수만큼 반복
for i in range(e):
    a, b = map(int, input().split())
    union_find(parent, a,b)




#각 원소가 속한 집합을 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()


#부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')










#부모테이블상에서 부모를 자기 자신으로 초기화


