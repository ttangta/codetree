def solution(num):
    answer = 0
    arr = list(num)

    for i in range(len(arr)):
        answer = answer * 2 + int(arr[i])

    return answer


num = input()

print(solution(num))