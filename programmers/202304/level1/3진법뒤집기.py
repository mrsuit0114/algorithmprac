def solution(n):
    answer = 0
    tmp = ""
    while n>=3:
        tmp += str(n%3)
        n = n//3
    tmp += str(n)

    answer = int(tmp,3)

    return answer

solution(45)