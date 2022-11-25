#문자열 뒤집기
data = list(map(int, input()))

check0= [0] * len(data)

check1= [1] * len(data)
cnt = 0

while True:

    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 1


    cnt +=1
    if data == check0 or data == check1:
        break



    for j in range(len(data)):
        if data[j] == 1:
            data[j] = 1
    cnt +=1
    if data == check0 or data == check1:
        break

print(cnt)

