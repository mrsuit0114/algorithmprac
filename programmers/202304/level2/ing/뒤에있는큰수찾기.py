def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []
    for i in range(len(numbers)):
        if stk:
            for i in reversed(stk):
                


    return answer


# 스택쓰는거같은데..
# numbers 앞에서부터 보면서 스택이 비어있으면 해당 값과 인덱스를 넣고
# 스택이 비어있으면 일단 넣고
# 스택이 안비어있으면 원소랑 비교

