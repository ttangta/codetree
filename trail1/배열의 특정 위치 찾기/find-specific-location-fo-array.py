arr = list(map(int, input().split()))

answer_1 = sum(arr[1::2])
arr_2 = arr[2::3]
print(f"{answer_1} {sum(arr_2)/len(arr_2):.1f}")