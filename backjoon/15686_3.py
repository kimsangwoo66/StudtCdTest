#치킨배달
#완전탐색

#풀이방안
#각 경우의 수의 집들과 치킨집과의 최소 거리들의 합들 중에서
#최소인 값을 출력
from itertools import combinations

n, m = map(int, input().split())

board = []


for i in range(n):
    board.append(list(map(int, input().split())))


chits = []
homes = []
result = int(1e9)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))

        if board[i][j] == 2:
            chits.append((i, j))

#치킨집을 선택할 수 있는 경우의 수 만큼 반복
for combi in combinations(chits, m):
    tot_result = 0

    #집의 개수만큼 반복
    for home in homes:
        distList = []

        # 고른 치킨집 m개씩 반복
        for chit in combi:
            distance = abs(home[0] - chit[0]) + abs(home[1] - chit[1])
            distList.append(distance)
        # 고른 치킨집들 중에서 거리가 최소값
        tot_result += min(distList)

        # 치킨집 m개를 골랐을떄의 경우에 수에서 도시의 치킨거리가 최소인 값
    result = min(result, tot_result)

print(result)




