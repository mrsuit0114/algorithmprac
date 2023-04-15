import heapq

def solution(scoville, K):
    answer = 0
    f=0
    flag = 0  # 가능 불가능
    count = 0
    heapq.heapify(scoville)

    while len(scoville)!=1 :  #한개인데 만족하는 경우 flag생각해야하는데
        f = heapq.heappop(scoville)  # 최소 스코빌 음식
        if f>=K :
            flag = 1
            break
        s = heapq.heappop(scoville)  # 두번째 최소 스코빌음식
        n = f + 2*s  #섞어서 만든 스코빌음식
        heapq.heappush(scoville,n)
        count+=1
    
    if scoville[0]>=K:
        flag=1

    answer = count if flag else -1

    print(answer)
    return answer

solution([1, 2],7)