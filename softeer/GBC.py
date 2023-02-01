"""
Gbc

알고리즘: 구현

조건
0m 부터 100m까지 일정 구간들의 엘리베이터 속도를 검사


구현아이디어

실제 제한구역과 검사구간의 속도를 뻇을때
최대가 되는 값을 출력

"""
import sys

input = sys.stdin.readline

n,m = map(int, input().split())


#실제 구간(구간길이, 제한속도)
limit_list = []
#검사 리스트(구간길이, 제한속도)
test_list = []

#최대로 제한속도를 넘어간 값
max_over = 0

for i in range(n):
    a,b = map(int, input().split())
    limit_list.append((a,b))


for j in range(m):
    a,b = map(int, input().split())
    test_list.append((a,b))

limit_speed = []
for m,s in limit_list:
    limit_speed = limit_speed + [s for i in range(m)]

test_speed = []
for m,s in test_list:
    test_speed = test_speed + [s for i in range(m)]

max_over = max([test_speed[i] - limit_speed[i] for i in range(100)])


if max_over >= 0:
    print(max_over)

else:
    print(0)






