#이코테 문자 재정렬
data = list(map(str, input()))
number = []
for i in data:
    if i.isdigit():
        number.append(int(i))
        data.remove(i)

data.sort()
total = sum(number)

joinStr = ''.join(data)

print(joinStr + str(total))



