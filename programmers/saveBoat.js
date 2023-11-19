function solution(people, limit) {
  let answer = 0;

  // 무거운 사람에서 가벼운 사람 순으로 내림차순
  people.sort(function(x,y) {
    return y - x
  })

  // 가장 무거운 사람 idx
  let left = 0

  // 가장 가벼운 사람 idx
  let right = people.length - 1


  // left가 right를 역전하면 모두 탈출
  while(left < right) {

    twoPeopleWeight = people[left] + people[right]

    if(twoPeopleWeight > limit) {

      // 1명 보트 탑승 후 탈출
      left += 1
    } else {
      // 2명 보트 탑승 후 탈출
      left += 1
      right -= 1
    }

    // 보트 증가
    answer += 1
  }


  // 역전하지 못하고 left와 right가 가리키고 있는 대상이 같을 경우
  // 태우지 못한 한사람이 남아있음
  if(left === right) {
    // 보트 증가
    answer += 1
  }
  return answer
}

var people = [70, 50, 80, 50]
var limit = 100
var result =solution(people, limit)

console.log('result: ', result)