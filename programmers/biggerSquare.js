// 답 참고 - 다시풀기
// DP(동적 프로그래밍) 사용 - 정답을 찾기 위한 패턴을 만들어야함
function solution(board)
{
    var answer = 0
    // 행길이 = 가로
    var rowCnt = board.length
    // 열길이 = 세로
    var colCnt = board[0].length


    if(rowCnt < 2 || colCnt < 2) {
      return 1
    }

    // 0번째 행 말고 1번째 행부터 시작
    for(var i=1; i<rowCnt; i++) {

      for(var j=1; j<colCnt; j++) {

        if(board[i][j] !== 0) {

          // 현재위치의 왼쪽 위의 대각선, 왼쪽, 위쪽의 값중 최소
          var minVal = Math.min(board[i-1][j-1], board[i-1][j], board[i][j-1])
          board[i][j] = minVal + 1
        }

        if(answer < board[i][j]) {
          answer = board[i][j]
        }
      }

    }

    return answer * answer;
}


var board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	

var result = solution(board)

console.log(result)