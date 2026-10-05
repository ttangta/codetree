arr_cnt = [0] * 4           

for i in range(3):
    info = tuple(input().split())
    
    if info[0] == "Y" and int(info[1]) >= 37:
        arr_cnt[0] += 1
    elif info[0] == "N" and int(info[1]) >= 37:
        arr_cnt[1] += 1
    elif info[0] == "Y" and int(info[1]) < 37:
        arr_cnt[2] += 1
    elif info[0] == "N" and int(info[1]) < 37:
        arr_cnt[3] += 1

for i in range(4):
    print(arr_cnt[i], end = " ")

if arr_cnt[0] >= 2:
    print("E")
