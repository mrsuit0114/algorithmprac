def solution(n):
    answer = 0
    ones = str(bin(n)).count('1')
    tmp = n+1
    while str(bin(tmp)).count('1')!=ones:
        tmp+=1
    answer=tmp
    return answer