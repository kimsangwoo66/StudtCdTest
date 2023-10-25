function solution(strings, n) {
    for (let i = 0; i < strings.length - 1; i++) {
        for (let j = i + 1; j < strings.length; j++) {
            if (strings[i][n] > strings[j][n] || (strings[i][n] === strings[j][n] && strings[i] > strings[j])) {
                // 두 문자열의 n번째 문자를 비교 or n번째 문자가 동일한 경우 전체 문자열을 비교
                const temp = strings[i];
                strings[i] = strings[j];
                strings[j] = temp;
            }
        }
    }
    
    return strings;
}