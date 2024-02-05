function solution(m, musicinfos) {
  var answer = '';
  var maxSpentTime = 0;

// musicinfos 순회
for(var music_info of musicinfos) {

  // 시작시간, 끝나는시간, 음악제목, 악보
  var [startTime, endTime, title, sheet] = music_info.split(',');

  // 악보에 대문자알파벳 + # 부분을 -> 소문자로 알파벳으로 치환
  sheet = sheet.replace(/(C#)/g,'c').replace(/(D#)/g,'d').replace(/(F#)/g,'f').replace(/(G#)/g,'g').replace(/(A#)/g,'a')
  
  var [startTime_hour, startTime_minute] = startTime.split(':')
  var [endTime_hour, endTIme_minute] = endTime.split(':')

  // 재생 시간 구하기
  var spendTime = (endTime_hour - startTime_hour) * 60 + (endTIme_minute - startTime_minute)

  // 악보길이
  var sheet_length = sheet.length

  var allSheet = '';

  // 음악 길이보다 재생 시간이 길 경우
  if(sheet_length < spendTime) {
    allSheet = sheet.repeat(spendTime / sheet_length + 1)

  } else if(spendTime < sheet_length) {
    // 음악 길이보다 재생 시간이 짦을 경우
    allSheet = sheet.slice(0,spendTime);
  } else {
    // 음악길이 == 재생 시간
    allSheet = sheet;
  }

  // 주어진 노래에 멜로디가 있는지 확인

  // 멜로디에 대문자알파벳 + # 부분을 -> 소문자로 알파벳으로 치환
  m = m.replace(/(C#)/g,'c').replace(/(D#)/g,'d').replace(/(F#)/g,'f').replace(/(G#)/g,'g').replace(/(A#)/g,'a')

    if(allSheet.includes(m)) {
      if(maxSpentTime < spendTime) {
        maxSpentTime = spendTime
        answer = title
      }
    }
  
}

  if(answer === '') {
    return "(None)"
  }

  return answer;
}

var m = "CC#BCC#BCC#BCC#B"
var musicinfos = 	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
var result = solution(m,musicinfos)


console.log(result)