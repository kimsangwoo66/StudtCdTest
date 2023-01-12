"""
가장 큰 증가 부분 수열

구현아이디어:

1.dp 리스트 생성
2.수열에서 자기보다 앞쪽에 있는 값들중 자신보다 작은 값의 인덱스를 찾는다.
3.해당 인덱스의 dp 값중 가장 큰 값과 자신의 값을 더해 dp에 다시 넣음
4.dp에서 max값을 출력


0부터 수열 크기-1 까지 순회 = i
 0부터 i번째가지 순회 = j
 수열[i] > 수열[j]:

시간복잡도: O(n^2)

"""

import sys
input = sys.stdin.readline

n = int(input())

slist = list(map(int, input().split()))

# 얕은 복사
#dp = slist

# 깊은 복사
dp = slist[:]

for i in range(n):
    for j in range(i):

        if slist[i] > slist[j]:
            dp[i] = max(dp[i], dp[j] + slist[i])

print(max(dp))
