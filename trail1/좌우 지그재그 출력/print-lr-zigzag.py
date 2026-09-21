def solution(n):
    for i in range(n):
        if i % 2 == 0:
            s = n * i + 1
            for j in range(n):
                print(s, end = " ")
                s += 1
        else:
            s = n * (i+1)
            for j in range(n):
                print(s, end = " ")
                s -= 1
        print()

solution(int(input()))