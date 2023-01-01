"""
좌표 압축

알고리즘:정렬, 구현

구현 아이디어

작은값부터 시작해서 0부터 인덱스를 부여하는 방법

"""

import sys

input=sys.stdin.readline

n = int(input())

nlist = list(map(int, input().split()))

slist = sorted(set(nlist))

d = {slist[i]: i for i in range(len(slist))}

print(d)

for v in nlist:
    print(d[v], end=" ")



