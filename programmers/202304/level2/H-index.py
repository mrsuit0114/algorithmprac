
def solution(citations):
    answer = 0
    citations.sort()
    for i in reversed(citations):
        if answer<i: # i가 같은경우는 하면안된다
            answer+=1
        else:break
        

    return answer

solution([25,8,5,3,3])

# 오름차순 정렬상태에서 뒤에서부터 h=1로 시작해서 h보다크면 한칸씩오면서 h+=1 하다가 안맞는순간

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

#각 원소별로 인덱스랑 비교해서 하는방법인건 똑같고 표현의 차이