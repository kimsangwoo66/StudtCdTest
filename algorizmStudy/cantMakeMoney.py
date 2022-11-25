#만들수 없는 금액
#동빈이가 만들 수 없 양의 정수 금액 중 최소값

#동전 중 하나만으로 만들 수없는경우
#동전들을 합쳐서 만들수 없는경우는


#각 동전으로 만들수 있는 값들
#

from itertools import combinations

N = input()
moneyUnit = list(map(int, input().split()))

moneyUnit.sort()
cnt = 0
value = 1
while True:

    for i in range(N):



    #화폐 단위 만큼 반복
    for coin in moneyUnit:

        if value % coin

    value += 1



print(value)

print(moneyUnit)