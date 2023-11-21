
// 순열 (순서 상관 있음)
function getCombinations(arr, combineNum) {
  let result = []; 

  if (combineNum == 1) {
      return arr.map((dr) => [dr])
  }
  // 조합할 수가 1이면 모든 배열의 원소 리턴

  arr.forEach((fixed, idx, origin) => {
      let rest = [];
      rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)]; 
      // => fixed값을 제외한 모든 값 겹치는 값이 있음 ( 순열 )
   

      let combination = getCombinations(rest, combineNum - 1); // 나머지에 대한 조합 값
      let attached = combination.map((br) => [fixed, ...br]); // 나온 결과 값에 대해 fixed값 붙어기
      
      result.push(...attached); // 리턴 배열에 넣어주기
  });

  return result
}

function solution(k, dungeons) {
  var answer = -1;

  // 유저가 탐험할 수 있는 최대 던전 개수
  var globalCnt = 0;
  dungeonsLength = dungeons.length

  // 유저가 던전을 탐색할 수 있는 모든 경우의 순서 리스트를 생성
  var allCaseSearchList = getCombinations(dungeons, dungeonsLength)

  // 모든 경우의 탐색 순서 순회
  allCaseSearchList.forEach(orderList => {

    var left_k = k

    //유저가 이번 경우에 탐험 할 수 있는 최대 던전 개수
    var thisOrderCnt = 0

    orderList.forEach(element => {
      
      //던전 탐험이 가능한 피로도가 남아있을 경우
      if(element[0] <= left_k) {
        left_k -= element[1]
        thisOrderCnt += 1
      }

    })


    if(globalCnt < thisOrderCnt) {
      globalCnt = thisOrderCnt
    }
  });


  answer = globalCnt
  
  return answer;
}