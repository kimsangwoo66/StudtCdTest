# 최소 힙

# 사용 알고리즘: 최소힙

# 조건
# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그값을 배열에서 제거한다.

# 구현 아이디어
# 최소 힙 라이브러리를 이용
import heapq
import sys

n = int(input())

xlist = []

for i in range(n):

            #input() 으로 작성하면 시간초과 발생!
    x = int(sys.stdin.readline())

    if x == 0:

        if len(xlist) == 0:
            print(0)
            continue

        m = heapq.heappop(xlist)
        print(m)

    else:
        heapq.heappush(xlist, x)














