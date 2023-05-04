from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    res = 0
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res += 1
    return res



# stk에 number[i]랑 남은게 k보다작으면 큰수가나오면 팝하고 교체하고 반복
# stk의 수랑 비교해서 9면 바로넣고, 크면 팝하고 넣고, 스택의 길이랑 k합쳐서
# 남은 number랑 같으면 다 넣고 스택 출력 


# 시간초과
# from itertools import combinations

# def solution(number, k):
#     answer = ''
#     cs = list(combinations(list(range(len(number))),len(number)-k))


#     for c in cs:
#         tmp = ""
#         for i in c:
#             tmp += number[i]
#         answer = max(tmp,answer)

#     return answer

# print(solution("1922341",3))

# 순서는 바꾸면안되네