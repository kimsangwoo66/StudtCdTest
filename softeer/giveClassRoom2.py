#강의실 배정

#알고리즘: heap

import heapq
import sys

input = sys.stdin.readline

n = int(input())

slist = []

for i in range(n):
    #강의 시작시간, 강의 끝나는 시간
    s,f = map(int, input().split())
    slist.append((s,f))

slist.sort()


end = 0


cnt = 0

while slist:

    #시작시간, 끝나는 시간
    a,b = heapq.heappop(slist)

    #강의 끝나는시간이 다음 강의시작 시간과 같거나 적은경우
    if b >= end:
        cnt += 1
        #다음 강의 시작 시간으로 변경
        end = a


print(cnt)
