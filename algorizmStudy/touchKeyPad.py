"""
키패트 누르기

알고리즘: 구현

조건
숫자가 2,5,8,0 일경우에
두 엄지 손까락의 위치에서 입력해야하는 숫자의 거리가 같을 경우
왼손잡이이면 왼손 이동
오른손잡이이면 오른손 이동


구현 아이디어

우선


입력되는 번호 만큼 반복

왼쪽 엄지손까락만 이동해서 가야하는 패드인지
오른쪽 엄지손까락만 이동해서 가야하는 패드인지 탐색

아닐경우 현재위치를 기반해서 center에 어떤 손까락이 와야할지 탐색


"""

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


def solution(numbers, hand):
    result = ""

    keyDick = {1:(0,0),2:(0,1),3:(0,2),
               4:(1,0),5:(1,1),6:(1,2),
               7:(2,0),8:(2,1),9:(2,2),
               '*':(3,0),0:(3,1),'#':(3,2)}

    lw = [1, 4, 7]
    rw = [3, 6, 9]

    left_hand = '*'
    right_hand = '#'
    for number in numbers:

        # 고른 번호가 왼손만 갈수있는 키패드에 있을경우
        if number in lw:
            result += "L"
            left_hand = number

        # 고른 번호가 오른손만 갈수있는 키패드에 있을경우
        elif number in rw:
            result += "R"
            right_hand = number

        # 고른 번호가 가운데 노여있는 키패드의 번호일 경우
        else:
            # 거리
            curpad = keyDick[number]

            lpad = keyDick[left_hand]
            rpad = keyDick[right_hand]

            lDistance = abs(curpad[0] - lpad[0]) + abs(curpad[1] - lpad[1])
            rDistance = abs(curpad[0] - rpad[0]) + abs(curpad[1] - rpad[1])


            if lDistance > rDistance:
                result += "R"
                right_hand = number

            elif lDistance < rDistance:
                result += "L"
                left_hand = number

                # 두 길이가 같은 경우
            else:
                if lDistance == rDistance:
                    if hand == "right":
                        result += "R"
                        right_hand = number
                    else:
                        result += "L"
                        left_hand = number

    answer = result
    return answer

result = solution(numbers, hand)

print(result)