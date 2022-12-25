#백준 140502 연구소

#사용 알고리즘 : 완전탐색 + bfs

#구현아이디어
# 1.안전영역 공간에 최대 벽 3개를 세웠을떄마다
# 2.깊이우선탐색을 사용해서 벽(1)안쪽의 공간에 전부 2로 채운다.
# 3. 그 후 안전영역 개수를 센다.
# 1, 2, 3을 끝까지 반복하고 안전영역의 최대값을 구한다 .


#의문점
# 안전영역공간에 최대 벽 3개를 세우는 모든 경우의 수를 어떻게 코드로 나타내지?
# 이부분에서 뇌정지 가 왔다.
# 백트래킹에 익숙해야 이문제를 해결할 수있다.

n, m = map(int, input().split())

graph = []
cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))


print(graph)


def solve():

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 1 or graph[i][j] != 2:
                graph[i][j] = 1


