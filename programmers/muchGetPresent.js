function solution(friends, gifts) {
  var answer = 0


  var friendsCnt = friends.length
  var giveGetList = new Array(friendsCnt)

  //선물지수
  var giftsIdxList = new Array(friendsCnt)

  //두 친구가 주고 받았다는 내용 기록 리스트 -> 플래그
  var giveGetListCk = new Array(friendsCnt)

  // 다음달 가장 많이 받는 친구의 선물 리스트
  var nextMonthMost = new Array(friendsCnt)
  
  // 각 리스트 초기화
  for (var i = 0; i < friendsCnt; i++) {
    giveGetList[i] = new Array(friendsCnt).fill(0)
    giveGetListCk[i] = new Array(friendsCnt).fill(0)
    nextMonthMost[i] = 0
    giftsIdxList[i] = 0
  }

  //console.log(nextMonthMost)

  for (var i = 0; i < friendsCnt; i++) {
    for (var j = 0; j < friendsCnt; j++) {
      if(i == j) {
        // 자기 자신일 경우
        giveGetList[i][j] = -1 
        giveGetListCk[i][j] = 1
      }
    }
  }

  

  gifts.forEach(element => {
    var first = element.split(" ")[0]
    var second = element.split(" ")[1]
    
    giveGetList[friends.indexOf(first)][friends.indexOf(second)] += 1

  });

  // 각 친구의 선물지수 구하기
  for(var i=0;i<friendsCnt;i++) {

    // 준선물
    var giveGift = 0
    // 받은선물
    var getGift = 0
    for(var j=0;j<friendsCnt;j++) {
      if(giveGetList[i][j] !== -1) {
        giveGift += giveGetList[i][j]
      }

      if(giveGetList[j][i] !== -1) {
        getGift += giveGetList[j][i]
      }
    }

    var giftIdx = giveGift - getGift
    giftsIdxList[i] = giftIdx

  }

  for(var i=0;i<friendsCnt;i++) {
    for(var j=0;j<friendsCnt;j++) {

      // 자기 자신 X && 주고받았는지 확인이 안되었을경우
      if(giveGetList[i][j] !== -1 && giveGetListCk[i][j] !== 1) {

        // 두사람이 선물을 주고 받은 기록이 있을 경우
        if(giveGetList[i][j] > 0 || giveGetList[j][i] > 0) {
          // 두 사람이 선물을 주고 받은 개수가 같을 경우
          if(giveGetList[i][j] == giveGetList[j][i]) {
            
            
            if(giftsIdxList[i] > giftsIdxList[j]) {
              nextMonthMost[i] += 1
            } else if(giftsIdxList[i] < giftsIdxList[j]) {
              nextMonthMost[j] += 1
            }

            // 두 친구가 주고 받았다는 내용 기록
            giveGetListCk[i][j] = 1
            giveGetListCk[j][i] = 1

          } else {
            // 받은 개수가 같지 않고 기록이 있을 경우
            if(giveGetList[i][j] > giveGetList[j][i]) {
              nextMonthMost[i] += 1
            } else {
              nextMonthMost[j] += 1
            }

            giveGetListCk[i][j] = 1
            giveGetListCk[j][i] = 1
          }
        }

        if(giveGetList[i][j] === 0 && giveGetList[j][i] === 0) {
          if(giftsIdxList[i] > giftsIdxList[j]) {
            nextMonthMost[i] += 1
          } else if(giftsIdxList[i] < giftsIdxList[j]) {
            nextMonthMost[j] += 1
          }
    
          giveGetListCk[i][j] = 1
          giveGetListCk[j][i] = 1
        }


      }
    }
    
  }
  
  answer = Math.max(...nextMonthMost)

  return answer;
}

var friends = ["muzi", "ryan", "frodo", "neo"];
var gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"];
// var friends = ["joy", "brad", "alessandro", "conan", "david"]
// var gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
var result = solution(friends, gifts);

console.log(result)