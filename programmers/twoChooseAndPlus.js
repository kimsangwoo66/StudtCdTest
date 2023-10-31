// 두개 뽑아서 더하기
function solution(numbers) {
  var answer = []
  var n1 = numbers.length
  for(let i = 1; i < n1; i ++ ) {
    var pointer = numbers[i-1];
    var numbers2 = numbers.slice(i);
    var n2 = numbers2.length
    
    for(let j=0; j<n2; j++) {
      if(answer.includes(pointer + numbers2[j])){
        continue
      }
      answer.push(pointer + numbers2[j])
    }
  }

  answer.sort(function(a,b) {
    return a - b
  })

  return answer
}


var numbers = [2,1,3,4,1]

var result = solution(numbers)

console.log(result)