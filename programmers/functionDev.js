function solution(progresses, speeds) {
  var answer = [];
  var releaseWait = []; 

  // 각 기능의 진도 배열 순회하며 작업이 끝나기까지 남은 일수 계산
  progresses.forEach((element, idx) => {
    console.log(element, idx)

    var finishDateCount = Math.floor((100 - element) / speeds[idx])
    if((100 - element) % speeds[idx] !== 0) {
      finishDateCount += 1
    }
    releaseWait.push(finishDateCount)
    console.log('releaseWait: ', releaseWait)
  });

  while(releaseWait.length !== 0) {
    var releasePoint = releaseWait.shift()
    var relaseCnt = 1


    while(releaseWait[0] <= releasePoint) {
      releaseWait.shift()
      relaseCnt += 1
    }
    answer.push(relaseCnt)
    
  }

  return answer;
}

// 각 기능의 진도 배열
var progresses = [90,90]
var speeds = [10,9]


var sol = solution(progresses, speeds)

console.log(sol)
