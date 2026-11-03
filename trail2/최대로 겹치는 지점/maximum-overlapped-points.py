OFFSET = 101
arr = [0] * OFFSET

def count(x1, x2):
    for i in range(x1, x2+1):
        arr[i] += 1

N = int(input())

for _ in range(N):
    x1, x2 = map(int, input().split())

    count(x1, x2)

print(max(arr))