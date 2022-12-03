# 뱀 - BOJ 3190
# 보드의 판 크기
# 덱 사용 (디큐)
# 뱀이 해당 좌표를 차지 하고 있는 중일떄 해당 좌표값이 2로 지정
# dx dy 우 하 좌 상

from collections import deque
#보드 판의 크기
n = int(input())

#사과 개수
k = int(input())

#게임판의 공간 초기화
board = [[0] * n for _ in range(n)]

#방향 전환
dx = [1,0,-1,0] #우 하 좌 상
dy = [0,1,0,-1]


#방향
direct = 0
change = deque()

for i in range(k):
    #해당 좌표에 사과 삽입
    n, m = map(int, input().split())
    board[n-1][m-1] = 1

time = 0
snake = deque()
snake.append((0,0))
board[0][0] = 2

#뱀의 방향전환 정보 개수
L = int(input())


for i in range(L):
    #반환전환 정보 큐에 삽입
    x, c = map(str, input().split())
    change.append((int(x), c))

def direct_change(c):
    global direct

    if c == 'L':
        if direct == 0:
            direct = 3

        else:
            direct -= 1


    else:
        if direct == 3:
            direct = 0

        else:
            direct += 1


def snakeGame():
    global time, direct

    #가장 앞에있는 방향 전환 시간과, 방향 전환 값 추출
    x, c = change.popleft()

    while True:
        #뱀의 몸의 길이가 1이라면 = 큐에 쌓인 튜플이 하나 일 경우
        if len(snake) == 1:
            tail_x, tail_y = snake[0]
            head_x, head_y = tail_x, tail_y
        else:
            #그게 아니라면 꼬리는 큐의 맨 왼쪽, 머리는 큐의 맨 오른쪽
            tail_x, tail_y = snake[0]
            head_x, head_y = snake[-1]
        nx = head_x + dx[direct]
        ny = head_y + dy[direct]
        time += 1

        #범위를 넘거나 뱀의 머리가 자신의 몸이 있는 좌표로 이동할 경우 종료
        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 or board[nx][ny] == 2:
            return


        #이동 좌표에 사과가 있을 경우
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            snake.append((nx,ny))

        #이동한 좌표에 사과가 없을 경우
        else:
            snake.popleft()
            board[tail_x][tail_y] = 0
            board[nx][ny] = 2
            snake.append((nx, ny))

        if x == time:
            direct_change(c)
            if len(change) > 0:
                x, c = change.popleft()
    return


snakeGame()

print(time)










