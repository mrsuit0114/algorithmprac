def solution(people, limit):
    answer = 0
    people.sort() #오름차순 정렬
    stk = []
    for i in range(len(people)-1,-1,-1):
        if stk:
            if stk[-1]+people[i]<=limit:
                stk.pop()
                answer+=1
            else:
                stk.append(people[i])
        else:
            stk.append(people[i])
    answer+=len(stk)

    return answer

#높은순서로 스택에넣으면서 두명의 합이 limit보다 작은순간만 팝하고 구명보트+1이후 스택에남은인원만큼추가


# def solution(people, limit) :
#     answer = 0
#     people.sort()

#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer

#투포인터를 활용한 방식
