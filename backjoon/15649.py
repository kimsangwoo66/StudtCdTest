#백준 N과 M

#알고리즘: 백트래킹

#조건
#1부터 N까 자연수 중에서 중복없이 m개 고른 수열
# 1 <= M <= N <= 8

#구현 아이디어

#1. 첫 for문에서 1 ~ N까지 하나를 선택
#2. 1에서 선택한 값을 제외하고 다음 for문 1~N값중 하나 선택
#3. M개가 선택되었을 경우 출력


n, m = map(int, input().split())


#수열 리스트
resultList = []
#방문 횟수
visited = [False] * (n+1)

#
def recur(num):

    #m개를 고를때 마다 출력 한뒤에 종료
    if num == m:
        print(' '.join(map(str, resultList)))
        return

    #i가 1~ n+1까지 반복
    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            resultList.append(i)

            recur(num+1)
            #이렇게 작성하면 동작이 재대로 되지 않는다.



recur(0)


