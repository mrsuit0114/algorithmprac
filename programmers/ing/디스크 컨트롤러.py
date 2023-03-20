import heapq

def solution(jobs):
    answer = 0
    heap = []  # 작업중에 들어온 일들을 넣어놓을 것 작업중 아니더라도 여기로 옮긴이후 실행하자
    answers = []  # 각 작업이 요청부터 작업종료까지 걸린 시간을 저장할 배열
    cur = 0  # 현재 시간
    jobs.sort(key = lambda job : (job[0],job[1]))  # 들어오는 순서, 짧은시간 대로 정렬하고 #동시에 들어오는경우도 생각
    
    if len(jobs) == 1:  # todo !!! 일이 하나인 경우
        answer = jobs[0][1]
        return answer

    #jobs는 앞으로 예정된 일, heap은 가능한 상황에서 바로 시작해야할 일들
    curjob = heapq.heappop(jobs)  # 가장 처음에 뽑는 일
    heapq.heappush(heap,[curjob[1],curjob[0]]) # 짧은시간우선
    while jobs or heap :
        curjob = heapq.heappop(heap)
        cur += curjob[0]  #시간 갱신
        answers.append([curjob[1],cur])  # 요청시간, 완료시간
        while jobs and cur >= jobs[0][0] :  # 작업중에 온 것들 일단 다 넣고 이걸 다하면 다시 바깥while가야되는데
            nextjob = heapq.heappop(jobs)
            heapq.heappush(heap,[nextjob[1],nextjob[0]])  # 작업시간, 요청시간

        # 아무것도 안하는 시간이 나오는 상황
        if jobs and not heap:  # 위에서 마침 힙을 다쓴 상황이라면?
            if jobs[0][0] > cur :  # 여기서 확인해줌 그런 상황 배제
                cur = jobs[0][0]  # 시간 갱신
                #todo 여기서 작업을 꺼내주거나 위에서 꺼내거나
                tmpjob = heapq.heappop(jobs)
                heapq.heappush(heap,[tmpjob[1],tmpjob[0]])
                # curjob = heapq.heappop(heap)
                continue
        
        # curjob = heapq.heappop(heap)

    print(answers)

    for a,b in answers:
        answer+=(b-a)
    answer = answer//len(answers)
    print(answer)

    return answer

solution([[0, 1], [1, 1], [50, 7]])

# import heapq

# def solution(jobs):
#     answer = 0
#     heap = []  # 작업중에 들어온 일들을 넣어놓을 것 작업중 아니더라도 여기로 옮긴이후 실행하자
#     answers = []  # 각 작업이 요청부터 작업종료까지 걸린 시간을 저장할 배열
#     cur = 0  # 현재 시간
#     jobs.sort(key = lambda job : (job[0],job[1]))  # 들어오는 순서, 짧은시간 대로 정렬하고 #동시에 들어오는경우도 생각
#     # print(jobs)
#     # heapq.heappush(jobs,[0,1])
#     # print(jobs)
    
#     if len(jobs) == 1:  # todo !!! 일이 하나인 경우
#         answer = 0

#     #jobs는 앞으로 예정된 일, heap은 가능한 상황에서 바로 시작해야할 일들
#     curjob = heapq.heappop(jobs)  # 가장 처음에 뽑는 일
#     while jobs and heap :
#         heapq.heappush(heap,[curjob[1],curjob[0]]) # 짧은시간우선
#         while cur >= curjob[0] :  # 작업중에 온 것들 일단 다 넣고
#             curjob = heapq.heappop(jobs)
#             heapq.heappush(heap,[curjob[1],curjob[0]])

#         curjob = heapq.heappop(heap)  # 작업시간, 요청시간 순서임!
#         cur += curjob[0]  #시간 갱신
#         answers.append([curjob[1],cur])  # 요청시간, 완료시간

#         if jobs and not heap:  # 위에서 마침 힙을 다쓴 상황이라면?
#             if jobs[0] > cur :  # 여기서 확인해줌 그런 상황 배제
#                 cur = jobs[0]
#                 curjob = heapq.heappop(jobs)

#         #while 끝에 curjob 갱신해줘야함







#     return answer

# solution([[0, 4], [1, 9], [2, 6],[2, 6]])



# import heapq

# def solution(jobs):
#     answer = 0
#     time = 0
#     heap = []
#     n = len(jobs)
#     jobs.sort(key=lambda x: x[0])  # 요청 시간 오름차순 정렬
    
#     while jobs or heap:
#         while jobs and jobs[0][0] <= time:
#             # 현재 시간 이전에 요청된 작업들을 모두 우선순위 큐에 넣음
#             start, duration = jobs.pop(0)
#             heapq.heappush(heap, (duration, start))
        
#         if not heap:
#             # 현재 처리할 작업이 없을 때
#             time = jobs[0][0]
#             continue
        
#         # 가장 작업 시간이 적은 작업을 처리함
#         duration, start = heapq.heappop(heap)
#         time += duration
#         answer += (time - start)
        
#     answer //= n
#     return answer

#gpt..