def is_carry(num1, num2):
    # 편의상 num1을 작은값으로 고정시킴
    # num1이 num2보다 크다면 swap
    if num1 > num2:
        num1, num2 = num2, num1

    clone1 = num1
    clone2 = num2

    while clone1 > 0:
        sum = (clone1%10) + (clone2%10)

        # carry가 발생한 경우이므로 바로 '이것은 carry이냐?' 라는 답으로 True 반환
        if sum >= 10: return True

        clone1 //= 10
        clone2 //= 10

    # while 반복문이 종료할 때 까지 carry가 발생하지 않았다면 '이것은 carry이냐?' 라는 답으로 Fasle 반환
    return False


def solution(N):
    # carry가 발생하는 상황이 아니라면 -1을 반환해야 함
    answer = -1

    for i in range(N-2):
        num1 = nums[i]
        for j in range(i+1, N-1):
            num2 = nums[j]
            # i번째 요소와 j번째 요소를 더하는 과정에서 carry가 발생하지 않았다면,
            if not is_carry(num1, num2):
                # 두 수의 합을 사용 하며 k 반복문 진입
                part_sum = num1 + num2
                for k in range(j+1, N):
                    num3 = nums[k]
                    if not is_carry(part_sum, num3):
                        answer = max(answer, (part_sum+num3))


    return answer



N = int(input())

nums = []

for _ in range(N):
    nums.append(int(input()))

print(solution(N))
