def solution(word):
    answer = 0
    arr = ["A","E","I","O","U"]
    for i in arr:
        tmp = i
        answer+=1
        if tmp==word:
            return answer
        for j in arr:
            tmp+=j
            answer+=1
            if tmp==word:
                return answer
            for k in arr:
                tmp+=k
                answer+=1
                if tmp==word:
                    return answer
                for l in arr:
                    tmp+=l
                    answer+=1
                    if tmp==word:
                        return answer
                    for m in arr:
                        tmp+=m
                        answer+=1
                        if tmp==word:
                            return answer
                        tmp = tmp[:-1]
                    tmp = tmp[:-1]
                tmp = tmp[:-1]
            tmp = tmp[:-1]
                            

    return answer

solution("AAAAE")

# 문자열 크기비교가 자동적으로 문자하나씩 비교하고, 같은경우 길이 비교까지 지원

# 다른사람 풀이

# from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
