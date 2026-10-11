N = 3
arr1 = [list(map(int, input().split())) for _ in range(N)]

input()

arr2 = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        value = arr1[i][j] * arr2[i][j]
        print(value, end = " ")
    print()