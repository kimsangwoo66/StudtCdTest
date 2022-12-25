
#n개중 m개를 고를 수있는 모든 경우의 수를 구해라. 중복 허용
#n<=8 까지
#백트래킹
#재귀함수를 사용
n ,m = map(int, input().split())

resultList = []
visited = [False] * (n+1)



def backtracking(cnt):
    if cnt == m:
        print(' '.join(map(str, resultList)))
        return


    for i in range(1, n+1):
        if visited[i] == False:

            visited[i] = True
            resultList.append(i)
            backtracking(cnt + 1)

            visited[i] = False
            resultList.pop()




backtracking(0)
