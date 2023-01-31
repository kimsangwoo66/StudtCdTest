import sys

input = sys.stdin.readline

n, k = map(int, input().split())

slist = list(map(int, input().split()))

alist = []

result = []

for i in range(k):
    a, b = map(int, input().split())
    alist.append((a,b))

for i in range(k):
    f, l = alist[i][0],alist[i][1]
    cnt = 0
    for j in range(f-1,l):
        cnt += slist[j]
    cnt = float(cnt / (l - f + 1))

    # round(2,344, d) d번째짜리 전에서 반올림
    cnt = round(cnt, 2)

    # 소수점 몇번째 자리까지 나타내기
    cnt = "%.2f" % cnt
    result.append(cnt)

for answer in result:
    print(answer)
