import sys
# 입력받은 모든 정수가 중복인 경우 결과로 출력할 -1의 값을 가진 정답 변수 초기화 및 할당
answer = -1

# N개의 정수를 입력받을 변수 
N = int(input())

# 입력받은 정수 N개를 리스트로 할당
nums = list(map(int, input().split()))[:N]


# nums 배열 중 값이 가장 큰 값을 찾기 위한 변수 생성 -> max_val+1 의 크기의 count 배열 생성 목적
max_val = -sys.maxsize

# nums 리스트를 순회하면서 최대값 갱신
for elem in nums:
    if max_val < elem:
        max_val = elem


# max_val+1 크기의 count 배열 생성
count = [0] * (max_val+1)


# nums 배열의 요소의 빈도수 체크
for elem in nums:
    count[elem] += 1

# count 배열의 뒤에서 부터 접근하여 값이 1인 경우를 answer에 재할당 후 바로 반복문 종료
for i in range(len(count)-1, -1, -1):
    if count[i] == 1:
        answer = i
        break

print(answer)