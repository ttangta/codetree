arr = list(map(int, input().split()))

arr_cnt = [0] * 11

for i in range(100):
    # 0점이 입력되면 반복이 남더라도 종료
    if arr[i] == 0:
        break

    value = arr[i] // 10

    arr_cnt[value] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {arr_cnt[i]}")