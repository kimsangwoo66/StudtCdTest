"""
숫자 카드 2

알고리즘: 정렬, 이분탐색

구현아이디어:
상근이가 갖고있는 숫자 카드 를 key: value 즉
숫자카드 숫자 : 그 숫자카드 개수 형태로 만든 뒤

어떤 수가 적혀있는 숫자카드를 상근이가 갖고있는지
유무를 확인한다.


시간복잡도 : O(1)


"""

import sys

input = sys.stdin.readline

n = int(input())

slist = list(map(int, input().split()))
sdict = {}

for i in slist:

    if i in sdict:
        sdict[i] += 1

    else:
        sdict[i] = 1


m = int(input())

compareList = list(map(int, input().split()))

for j in compareList:
    if j in sdict:
        print(sdict[j], end=" ")

    else:
        print(0, end=" ")







