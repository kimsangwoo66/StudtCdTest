#문자열 압축
#완전 탐색
#슬라이드 잘 활용하기
def solution(s):

    result = []




    # i단위로 자르기
    for i in range(1, len(s)+1):

        # i번째까지 미리 자르기
        tmp = s[:i]
        # 문자 조립
        makeStr = ''
        cnt = 1
        #i단위로 끝까지 반복
        for j in range(i, len(s) + i, i):

            #i단위로 자른 값중에 값이 같다면
            if tmp == s[j:i+j]:
                cnt += 1

            else:
            #아니라면
                if cnt != 1:
                    makeStr = makeStr + str(cnt) + tmp

                else:
                    makeStr = makeStr + tmp

                #다음 자른 값으로 tmp변경
                tmp = s[j:i+j]
                cnt = 1

        result.append(len(makeStr))



    return min(result)



s = "aabbaccc"
#s = "ababcdcdababcdcd"
#s = "abcabcdede"

result = solution(s)

print(result)