from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    visit =[0] * (n+1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    dq = deque([1])

    visit[1]=1

    while dq:
        cur = dq.popleft()  #현재 노드 번호
        for node in graph[cur]:  #방문 가능노드 번호
            if visit[node] == 0 : #아직 방문안했다면
                dq.append(node)
                visit[node] = visit[cur]+1

    k = max(visit)  #sort사용도 괜찮네
    answer = visit.count(k)

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))