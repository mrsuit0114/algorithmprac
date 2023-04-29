# 다른사람 힌트 2차원배열을 좌표로 봤을때 xy중 큰값이 해당 값

import math

def solution(n, left, right):
    answer = []
    lr = math.ceil(left/n)
    lc = left%n
    rr = math.ceil(right/n)
    rc = right%n

    for i in range(lr,rr+1):
        tmp = [i]*i
        for j in range(i,n):
            tmp.append(j+1)
        answer+=tmp
    
    answer = answer[lc:n*(rr-lr)+rc+1]

    return answer

# tc 1,2 실패.. 왜지 처리시간이랑 용량보면 특수한상황은 아닌거같은데

solution(3,2,5)


# def solution(n, left, right):
#     answer = []
#     for i in range(1,n+1):
#         for j in range(i):
#             answer.append(i)
#         for k in range(i,n):
#             answer.append(k+1)

#     return answer[left:right+1]


# 슬라이싱이 필요한 부분까지만 배열을 만들어야함
# 우선 필요한 행을 1차원 배열로 만들고 이후 슬라이싱하자
# i부터 k행까지 필요한 경우 ans= ans+[i]*i, for (i,n): ans.append(j+1)


# 2차원배열 만들지말고 1차원 배열 만들어서 슬라이싱하자

# 실제로 배열을 만들 필요는 없어보이는데
# idx에따라서 몇번째줄의 어디부터인지만 알면 규칙에따라 배열생성 가능할 듯
# n이 4고 7부터 14를 원할때 2행의 끝부터 4행의 3번째까지
#2행은 2234
#3행은 3334
# 각 행은 i행만큼 i가 반복된 후 끝까지 1씩 증가하는 배열의 형태를 가짐

