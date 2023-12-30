function solution(s) {  
  var answer = -1

  var opener = ['(','{','[']
  var closer = [')','}',']']
  var cnt = 0

  for(var i = 0 ; i < s.length ; i++) {

    // 회전 상태
    var rot = s.slice(i) + s.slice(0,i)
    var isPair = true
    var stack = []

    for(var j = 0; j < s.length; j++) {

      // 여는 괄호일 경우
      if(opener.includes(rot[j])) {
        stack.push(rot[j])

      } 
      // 닫는 괄호일 경우
      else if(opener[closer.findIndex(v => v === rot[j])] === stack[stack.length - 1]) {
        
        stack.pop()

      } else {
        isPair = false
        break

      }
    }

    // 검사가 true이고 스택이 비어있을 경우
    if(isPair && stack.length === 0) {
      cnt += 1
    }
    
  }

  answer = cnt

  return answer;
}