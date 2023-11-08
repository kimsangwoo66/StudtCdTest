function solution(fees, records) {
  const carRegist = {};
  const total = {};
  const answer = [];

  let rc = records.length
    // 배열의 요소 할당
  for (const i = 0; i < rc ; i++) {
    // 누적 시간 계산
    const [time, carNum, inoutYN] = records[i].split(" ");

    // 시간을 분 단위로 쪼개기
    const [hour, minutes] = time.split(":");
    const currentTime = parseInt(hour) * 60 + parseInt(minutes);

    if (carNum in carRegist) {
      // 입차했다가 출차 할 경우
      total[carNum] = (total[carNum] || 0) + (currentTime - carRegist[carNum]);
      delete carRegist[carNum];
    } else {
      // 입차할 경우
      carRegist[carNum] = currentTime;
    }
  }

  // 입차했는대 출차를 안할 경우
  const maxTime = 23 * 60 + 59;
  for (const num in carRegist) {
    total[num] = (total[num] || 0) + (maxTime - carRegist[num]);
  }

  // 요금 계산
  const [defaultTime, defaultMoney, additionalTime, additionalFee] = fees;

  for (const num in total) {
    let cost = defaultMoney;
    if (total[num] > defaultTime) {
      cost += Math.ceil((total[num] - defaultTime) / additionalTime) * additionalFee;
    }
    answer.push([num, cost]);
  }

  answer.sort((a, b) => a[0].localeCompare(b[0]));

  return answer.map((value) => value[1]);
}