def solution(s):
    answer = -1
    stk =[]
    for i in range(len(s)):
        if stk :
            if stk[-1] == s[i]:
                stk.pop()
            else :
                stk.append(s[i])
        else:
            stk.append(s[i])

    return not(answer)

    # if stk :
    #     answer = 0
    # else :
    #     answer = 1
    # return answer


# aaa일때는 어딜지우든 하나 남으니까 결과는 같음
# 하나씩 스택에 넣으면서 비교할건데 같으면 스택에서 팝 다르면 넣었을때 스택에 남으면 0 아니면1

