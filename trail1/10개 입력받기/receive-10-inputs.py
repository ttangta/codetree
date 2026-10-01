arr = list(map(int, input().split()))

sum_v = 0
for i in range(10):
    # 배열에 i번째 값이 0이면 해당 인덱스 이전까지 슬라이싱
    if arr[i] == 0:
        arr = arr[:i]
        break

print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")


    