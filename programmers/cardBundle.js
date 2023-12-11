function solution(cards1, cards2, goal) {
  var answer = 'Yes';
  goal.forEach(element => {
    if(cards1[0] === element) {
      var card1Pop = cards1.shift()
      console.log(card1Pop)
    }
    else if(cards2[0] === element) {
      var card2Pop = cards2.shift()
      console.log(card2Pop)
    }
    else{
      return answer = 'No'
     }

  });

  return answer;
}

var card1 = ["i", "water", "drink"]
var card2 = ["want", "to"]

var goal = ["i", "want", "to", "drink", "water"]
var result = solution(card1, card2, goal)

console.log(result)