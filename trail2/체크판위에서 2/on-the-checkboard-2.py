def solution(R, C):
    answer = 0
    if arr[0][0] == arr[R-1][C-1]:
        return 0
    # (0,0) 의 우측 하단 대각선 지점을 탐색 구간의 시작지점으로 지정한 후 조건에 맞는 부분 찾기
    # 조건 1: arr[0][0]의 값과 달라야함
    # 조건 2 : 조건 1을 만족하면서 해당 i,j 에 각 1을 더한 값이 N * N 배열 범위 내의 값이 어야 -> 해당 조건으로 한 번에 마지막 요소에 접근하는 경우도 막음
    for i in range(1, R):
        for j in range(1, C):
            # 조건 1, 2를 만족했다면 해당 위치에서 우측 하단 대각선 지점부터 조건에 맞는 부분 찾기
            # 조건 1 : arr[i][j]의 값과 달라야함
            # 조건 2 : 조건 1을 만족하면서 k, z에 각 1을 더한 값이 N * N 배열 범위 내의 값이어야 함
            if arr[i][j] != arr[0][0] and i+1 < R and j+1 < C:
                for k in range(i+1, R):
                    for z in range(j+1, C):
                        if arr[k][z] != arr[i][j] and k+1 < R and z+1 <C:
                            answer += 1
    return answer

R, C = map(int, input().split())
arr = [list(input().split())[:C] for _ in range(R)]
print(solution(R, C))