#귤 고르기 복습

#귤 k를 고를떄 서로다른 종류의 수의 최소 값
def solution(k, tangerine):

    #귤별로 딕셔너리 만들기
    Olist = {}
    Osum = 0
    answer = 0

    for i in tangerine:

        if i not in Olist:
            Olist[i] = 1

        else:
            Olist[i] += 1


    Olist = sorted(Olist.items(), key=lambda x:x[1], reverse=True)


    for i in Olist:
        Osum += i[1]
        answer += 1
        if k <= Osum:
            return answer

    return answer





k = 4

tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

result = solution(k, tangerine)


print(result)
