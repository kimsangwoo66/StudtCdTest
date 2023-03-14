"""
1700 멀티테스깅

구현아이디어:

1.다신 사용안할 전자기기의 플러그를 우선 뽑기
2.다시 사용할 전자기기를 가장 나중에 뽑기

"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

itemlist = list(map(int, input().split()))

plugin = []
cnt = 0


for i in range(k):
    #이미 꽃혀있는 전자기기일 경우 스킵
    if itemlist[i] in plugin:
        continue

    #비어있는 플러그가 있을 경우
    if len(plugin) < n:
        plugin.append(itemlist[i])
        continue


    #비어있지도 않고 이미 꽃혀있는 전자기기가 아닐 경우

    idx_list = []
    for j in range(n):

        #사용해야할 전자기기 중에 이미 플러그에 꽃혀 잇는 경우
        if plugin[j] in itemlist[i:]:
            idx = itemlist[i:].index(plugin[j])

        else:
            # 다시 사용할 일이 없는 전자기기일 경우
            idx = 101
        idx_list.append(idx)

    # 사용할일이 없는 전자기기를 우선 뽑는다. -> #느리게 사용될 전자기기를 우선으로 뽑음. (플러그를 뽑는 최소 회수를 구하기 위해서)
    plugOut = idx_list.index(max(idx_list))

    del plugin[plugOut]
    plugin.append(itemlist[i])
    cnt += 1

print(cnt)









