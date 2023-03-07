"""
조건
귀금속은 톱으로 자르면 잘려진 부분의 무개만큼 가치를 가짐

알고리즘: 그리디?

구현아이디어
# nlist 0번째 금속의 무게 90, 무게당가격 1
# nlist 1번째 금속의 무게 70, 무게당가격 2
# 1번째 총금액 140 + 0번째 총금액 30원


"""

import sys

input = sys.stdin.readline

# 배낭 무게 w , 귀금속 종류 n
w, n = map(int, input().split())

itemlist = [list(map(int, input().split())) for _ in range(n)]


itemlist = sorted(itemlist, key=lambda x:x[1], reverse=True)

cost = 0
# 무게당 금속이 가장 비싼 순서로 나열
for item in itemlist:

    # 가방의 여유 공간이 있을경우
    if w > item[0]:
        cost += item[1] * item[0]
        w -= item[0]

    # 가방의 수용량이 전체 무게 다 적을 경우
    else:
        cost += w * item[1]
        break

print(cost)


















