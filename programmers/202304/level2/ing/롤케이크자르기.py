def solution(topping):
    answer = 0
    for i in range(len(topping)):
        s1 = set(topping[:i])
        s2 = set(topping[i:])
        if len(s1)==len(s2):
            answer+=1


    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))


