#볼링공 고르기
#볼링공의 개수와 공의 최대 볼링공의 무게에 관계없으 리스트 데이터 만으로 해결
#볼링공의 최대 무개는 10


#볼링공의 개수 N, 공의 최대 볼링공 무게 M
N, M = map(int, input().split())

#각 볼링공의 무게
data = list(map(int, input().split()))

arr = [0] * 11
result = 0
for i in data:

    arr[i] += 1

#1~부터 최대무개(M)까지의 무게에 대해 처리
for i in range(1, M+1):
    #무개가 i인 볼링공에 대한 개수 제외  (A가 선택할 수 있는 개수
    N -=arr[i]

    #B가 선택할 수 있는 개수
    result += arr[i] * N


print(result)


