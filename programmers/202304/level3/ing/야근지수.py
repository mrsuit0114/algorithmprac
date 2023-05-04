def solution(n, works):
    answer = 0
    works
    return answer

# 큰 값을 우선으로 낮추는게 중요함
# 내림차순 정렬하고 뒤의 원소보다 작아질때까지 값을 내리고 같으면 남은 값에 따라 세번째
# 원소랑 같아질때까지 또 내리고.. 이거 번거로운데 한번에 계산 어떻게할까
# 빼는건 문제가안되는데 같아지는순간 계속 하나씩 빼는게 문제되는데



# n을 사용해서 최대한 크기가 고르게 되는것이 값이 작을 것이라고 가정
# 애초에 골고루 되어있으면 합을구하고 n을 뺸 후 works의 길이만 큼 나누면 되는데..
# 이를 착안해서 모두의 합을 구하고 갯수만큼 나눈다음 최대값을구해
# 원래의 works의 최대값에서 n을 뺐을때 이 크기보다 작으면 채용
# 보다 크면 불가능하기 때문에 전부다 큰쪽을 빼서 리턴하면될듯함
# 안되는 예외가 많은데 틀린 알고리즘인듯 6,6,6,1,1,1 n=3 일때 딱봐도안됨

# import math

# def ret(works):
#     ans = 0
#     for t in works:
#         ans+=t**2
#     return ans


# def solution(n, works):
#     answer = 0
#     works.sort()
#     maxwork = works[-1]
#     tmpsum = sum(works)-n
#     if tmpsum<=0:
#         return 0
#     average = math.ceil(tmpsum/len(works))
#     if maxwork > average :
#         works[-1] -= n
#         answer = ret(works)
#     else:
#         for j in range(tmpsum%len(works)):
#             answer+= average**2
        
        

#     return answer


