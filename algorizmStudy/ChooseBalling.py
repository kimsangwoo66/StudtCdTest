#볼링공 고르기
#볼링공의 개수와 공의 최대 볼링공의 무게에 관계없으 리스트 데이터 만으로 해결
#이방법으로 푸는게 아닌것 같다. 다시 풀어봐야할 문제

from itertools import combinations

#볼링공의 개수 N, 공의 최대 볼링공 무게 M
N, M = map(int, input().split())

#각 볼링공의 무게
data = list(map(int, input().split()))
combi = list(combinations(data, 2))
cnt = 0

for i in combi:
    if i[0] == i[1]:
        continue
    cnt +=1

print(cnt)


