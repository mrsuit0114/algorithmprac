from collections import deque

def solution(prices):
    answer = deque([])
    minval = 10001
    stk = []
    for i in range(len(prices)-1,-1,-1):
        if prices[i]<=minval: # minval보다 작거나 같음
            minval = prices[i]
            answer.appendleft(len(stk))
            # answer.insert(0,len(stk))
        else:
            for j in range(len(stk)-1,-1,-1):
                if prices[i]>stk[j]:
                    # answer.insert(0,len(stk)-j)
                    answer.appendleft(len(stk)-j)
                    break
        stk.append(prices[i])


    return list(answer)

# 다른사람풀이인데 메모리는 1~2mb 약간적고 시간은 1.5배이상

# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer

#break 추가하고 답은 맞는데 효율성에서 시간초과 n^2
# deque로 쓰면 통과함
# def solution(prices):
#     answer = []
#     minval = 10001
#     stk = []
#     for i in range(len(prices)-1,-1,-1):
#         if prices[i]<=minval: # minval보다 작거나 같음
#             minval = prices[i]
#             answer.insert(0,len(stk))
#         else:
#             for j in range(len(stk)-1,-1,-1):
#                 if prices[i]>stk[j]:
#                     answer.insert(0,len(stk)-j)
#                     break
#         stk.append(prices[i])


#     return answer

# 알고리즘이 틀렸나 실패나오네
# 중간에 break 빼먹었었음
# def solution(prices):
#     answer = []
#     minval = 10001
#     minidx = 0
#     stk = []
#     for i in range(len(prices)-1,-1,-1):
#         if prices[i]<=minval: #최소값보다 작거나같으면
#             minval = prices[i]
#             minidx = i
#             answer.append(len(stk)) #해당 스택의 크기만큼 안떨어진것이고
#         else: # 최소값보다 크면
#             for j in range(len(stk)-1,-1,-1): #스택을 검사해봐야지
#                 if prices[i]>stk[j]: # 검사하다가 작은값이 나오면
#                     answer.append(len(stk)-j) # 
#         stk.append(prices[i])


#     return answer[::-1]

print(solution([1,2,3,2,3]))

# a>min 상황에서 a>b>min을 만족하는 b를 확인해야함  

# 뒤에서부터 계산해서 스택을 활용하는것 같은데
# 스택의 최소값보다 작을때만 확인하기?
# 크면 스택의 크기만큼 값을갖는거고 작으면? len(stk) - minvalidx 의값을 가진다
# 가격이 최소값보다 작으면 스택의 길이만큼의 값을 갖고, 최소값보다 클때 최소값은아니지만 해당 가격보다
# 작은 값이 있을지도 모르기때문에 계산을 해야되는데? 어쩔수없이 해야하나
# for i in range(len(stk)-1,minidx,-1):
# 해서 값이 더 작은게 있으면 값을 주고 없으면 len(stk) - minidx
# 이렇게하는게아닌듯?