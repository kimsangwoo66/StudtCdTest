# 전체 스테이지 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 스테이지에 도달한 유저가 없다면 해당 스테이지의 실패율은 0
# 실패율이 높은 스테이지 부터 내림차순으로 스테이지 번호가 담겨있는 배열 return

from collections import defaultdict
def solution(N, stages):

    #스테이지별 실패률
    FailResult = {}
    answer = []
#stages = [2, 1, 2, 6, 2, 4, 3, 3]
    #1~ n번째 스테이지 까지
    for i in range(1, N+1):
        #클리어하지 못한 사용자수
        Ncnt = 0

        # 해당 스테이지에 도달한 플레이어수
        Icnt = 0

        for j in stages:
                #해당 스테이지에 도달했으나 아직 클리어 못한 경우
            if j == i:
                Ncnt += 1

                #해당 스테이지에 도달한 플레이어수
            if i <= j:
                Icnt +=1

        #해당 스테이지에 도달한 플레이어수가 0일 경우
        if Icnt == 0:
            FailRate = 0

            # 해당 스테이지 실패율계산
        else:
            FailRate = Ncnt / Icnt

        #각 스테이지별 실패율 모음
        FailResult[i]= FailRate


        #실패율이 높은 순서로 스테이지 오름차순 정렬,
        # #딕셔너리에 key옵션에 딕셔너리.get옵션시 해당 딕셔너리의 value를 바탕으로 계산한 key값을 반환
    answer = sorted(FailResult, key=FailResult.get, reverse=True)
    return answer

#체크


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

result = [3,4,2,1,5]

clear = solution(N,stages)

print(clear)