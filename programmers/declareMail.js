function solution(id_list, report, k) {
    // declareObj: 유저가 신고한 ID 오브젝트 선언,
     // ex) {"muzi": ["forodo", "neo"]}
     let declaredObj = {}
    
    // declaredCnt: 유저별 신고당한 횟수 오브젝트 선언
     // ex) {"muzi": 1}
     let declaredCnt = {}    

     // 오브젝트 초기값 세팅
     id_list.forEach(element => {
        declaredObj[element] = []
        declaredCnt[element] = 0
     });
     
    // 유저별 처리 결과 메일 받은 횟수
    var answer = []

   
    // 유저가 신고한 ID 오브젝트 저장
    // report 순회
    for(let i = 0 ; i < report.length; i ++) {
        // 띄어 쓰기된 곳을 찾아서 앞, 뒤로 쪼갬
        var fb = report[i].split(' ');
        // 앞
        var f = fb[0]
        // 뒤
        var b = fb[1]
        
        // declareObj에 키(앞) = value(뒤 저장)에 이미 존재할 경우 스킵
        if(declaredObj[f].includes(b)) {
            continue
        }
        // declareObj에 키(앞) = value(뒤 저장)
        // declaredCnt 키(앞)) = 카운트 + 1
        declaredObj[f].push(b)
        declaredCnt[b] += 1
        
    }

        
    // id_list의 순서 순회
    for(let i = 0; i < id_list.length; i ++) {
        let cnt = 0
        for(let j = 0; j < declaredObj[id_list[i]].length; j++) {
           let v = declaredObj[id_list[i]][j]
           // 만약 declaredCnt[v] >= k 경우
           if(declaredCnt[v] >= k) {
            cnt ++
           }
            
        }
        answer.push(cnt)
    }
        // cnt = 0
        // declareObj에 id_list[i]를 넣어서 순회 (값:j)

    return answer;
}

var id_list = ["muzi", "frodo", "apeach", "neo"]
var report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

var k = 2

var result = solution(id_list, report, k)

console.log('결과: ', result)

