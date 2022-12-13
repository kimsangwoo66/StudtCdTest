# 최대힙
# 최대힙 자료구조 사용

#구현아이디어
#1. 최소 합을 뒤집기

#1, 2, 3 ,4 ,5 를 각각 *(-1) 을 해서 push

#heapq 에 -5 ,-4, -3, -2, -1 로 정렬됨

#heapq에서 다시 *(-1) 을 해서 pop

import sys
import heapq

xlist = []
hp = []
input = sys.stdin.readline

n = int(input())


for i in range(n):
    x = int(input())

    if x == 0:

        #리스트가 비었을 경우
        if len(xlist) == 0:
            print(0)
            continue


        m = -heapq.heappop(xlist)
        print(m)

    else:
        heapq.heappush(xlist, -x)
