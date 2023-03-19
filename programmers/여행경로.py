import copy

def solution(tickets):
    answer = []
    graph = {}  # 원본 그래프
    visit = {}  # 방문가능횟수를 저장할 dic
    for ticket in tickets:
        start = ticket[0]
        dest = [ticket[1]]
        if start in graph :
            dest += graph[start]
        graph[start] = sorted(dest)
        if dest in visit :
            visit[dest]+=1
        else :
            visit[dest] = 1

    

    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# import copy

# def solution(tickets):
#     answer = []
#     temp = {}  # 각 테스트케이스별 가능한 경로를 저장할 딕
#     graph = {}  # 원본 그래프
#     for ticket in tickets:
#         start = ticket[0]
#         dest = [ticket[1]]
#         if start in graph :
#             dest += graph[start]
#         graph[start] = sorted(dest)
#     #중복방문이 가능할 수도 있고 어차피 뺄거라 방문처리는 따로 필요없다
#     #종료시점을 어떻게 확인?
#     #모든 키값의 value가 0 또는 티켓 갯수만큼, 후자가 좋아보임
#     def dfs(depth, start,test):  #남은 티켓갯수, 현재 지점, test 번호
#         nonlocal graph
#         nonlocal answer
#         answer.append(start)
#         if depth == 0:
#             return

#         next = graph[start][0]
#         tempgraph[start].remove(next)
#         dfs(depth-1,next,test)

#     count = 0

#     while True:
#         dfs(len(tickets),"ICN",count)
#         count+=1



#     return answer

# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))