function solution(maps) {

  // 맵의 가로 길이
  var xLength = maps.length
  // 맵의 세로 길이
  var yLength = maps[0].length
  // 왼쪽, 오른쪽 방향 리스트
  var direct_x = [-1, 0, 1, 0]
  // 위, 아래 방향 리스트
  var direct_y = [0, -1, 0 , 1]

  function bfs(x,y) {
    var q = []
    q.push([x,y])
    
    while(q.length > 0) {
      //리스트 앞에서 부터 꺼냄
      var [x,y] = q.shift()
  
      for(var i = 0 ; i < 4; i++) {
  
        var nx = x + direct_x[i]
        var ny = y + direct_y[i]
  
        // 맵에서 벗어났을 경우
        if(nx < 0 || nx >= xLength || ny < 0 || ny >= yLength) {
          continue
        }
  
        // 벽일 경우
        if(maps[nx][ny] == 0) {
          continue
        }
  
        // 길이 존재할 경우
        if(maps[nx][ny] == 1) {
          maps[nx][ny] = maps[x][y] + 1
          q.push([nx, ny])
        }
      }
  
    }
    
    // 상대 진영에 도달하지 못했을 경우
    if(maps[xLength -1][yLength - 1] < 2) {
      return -1
    }
  
    return maps[xLength -1][yLength -1]
  }

  var answer = bfs(0,0)

  return answer
}


var maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


var result = solution(maps)

console.log(result)