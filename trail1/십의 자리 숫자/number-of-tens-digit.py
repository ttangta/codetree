arr_cnt = [0] * 10
arr = list(map(int, input().split()))

for a in arr:
    # a가 0이면 카운팅 종료
    if a == 0: break

    value = a // 10
    arr_cnt[value] += 1

# arr_cnt의 인덱스 = arr 원소의 10의 자리 이때 출력 예시는 1부터 시작
for i in range(1, 10):
    print(f"{i} - {arr_cnt[i]}")
