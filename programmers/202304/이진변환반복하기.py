
def solution(s):
    answer = []
    count=0 #횟수
    removed = 0 # 0지운 갯수
    while s!='1':
        removed += s.count('0')
        s = bin(len(s)-s.count('0'))[2:]
        count+=1
    answer = [count,removed]

    return answer

print(solution("110010101001"))
print("")


# 재귀로해야하나 규칙이 독특한데 쉽게표현되는 수식이 있으려나
