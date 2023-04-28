def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []
    for i in range(len(numbers)):
        if stk :
            while stk and stk[-1][0]<numbers[i]:
                tmp = stk.pop()
                answer[tmp[1]] = numbers[i]
        stk.append([numbers[i],i])


    return answer


# 스택에 (값,idx)넣고 number와 비교,number가 작거나 같으면 스택에 넣고, 큰동안 pop

