from collections import deque

def solution(n, computers):
    answer = 0
    # graph = [[]] * n  이렇게하면 배열이 개별적으로 되는게 아닌거같네
    graph = [[] for i in range(n)]  # 참..

    #그래프로 표현하기 인접리스트
    for i in range(len(computers)):
        for j in range(len(computers)):
            if computers[i][j]==1:
                graph[i].append(j)

    network=0
    visit = [0] * n


    for i in range(n):
        if visit[i]== 0:
            dq = deque([i])
            network+=1
        while dq :
            cur = dq.popleft()
            visit[cur] = 1
            for com in graph[cur]:
                if visit[com] == 0:
                    dq.append(com)

    answer = network

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             # for i in range(len(computers)-1, -1, -1):
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer