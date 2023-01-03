"""
크레인 인형뽑기 게임

알고리즘:

조건
크레인 작동시 인형이 집어지지 않는 경우는 없으나,
if 인형이 없는 곳에서 크레인을 작동 시킬 경우
아무일도 일어나지 않음

구현 아이디어


"""

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):

    # 계산하기 쉽게 그래프에 0번째 추가
    for i in range(len(board)):
        board[i] = [0] + board[i]
    q = []
    cnt = 0

    #크레인 이동
    for move in moves:

        #게임화면 탐색
        for i in range(1, len(board)):
            if board[i][move] > 0:
                q.append(board[i][move])
                board[i][move] = 0
                if len(q) > 1 and q[-1] == q[-2]:
                    cnt += 2
                    del q[-1]
                    del q[-1]
                break
    answer = cnt
    return answer


result = solution(board, moves)

print(result)
