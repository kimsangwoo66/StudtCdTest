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
    heapq.heappush(slist, (f,s))
    #slist.append((f,s)) #리스트에 추가해서 sort하면 시간초과에러 .. 왜?

#slist.sort()

#초기값
ch = 0
cnt = 0

while slist:

    #끝나는시간, 시작시간
    f,s = heapq.heappop(slist)

    #현재 수업의 끝나는시간이 다음수업의 시작시간보다 작거나 같을경우
    #다음 수업의 시작시간이  현재 수업의 끝나는시간 보다 크거나 같을 경우
    #서로 같음

    #시작시간이 초기값(끝나는시간) 보다 크거나 같으면 카운트
    if s >= ch:
        cnt += 1
        #다음 강의 시작 시간으로 변경
        ch = f


print(cnt)
