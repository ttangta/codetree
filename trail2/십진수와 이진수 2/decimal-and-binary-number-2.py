def solution(N):
    N = list(map(int, list(N)))

    num = 0
    for i in range(len(N)):
        num = num * 2 + N[i]

    num *= 17

    arr = []

    while num > 0:
        arr.append(num%2)
        num //= 2


    answer = ""
    for i in range(len(arr)-1, -1, -1):
        answer += str(arr[i])

    return answer

N = input()

print(solution(N))