"""
회의실 예약

알고리즘: 우선순위 큐

구현 아이디어

힙이랑 어째 비슷하다
"""
import heapq
from collections import defaultdict


#회의실의 수: n, 예약된 회의실의 수: m
n,m = map(int, input().split())

conferList = {}

for i in range(n):
    conferList[input()] = ()

for i in range(m):
    r,s,t = map(str, input().split())
    s=int(s)
    t=int(t)
    if r in conferList:
        conferList[r] += (s,t)


    print(conferList)