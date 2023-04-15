from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visit = []
    for i in range(n):
        visit.append([0]*m)

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    dq = deque([(0,0)])
    visit[0][0] = 1

    while dq :
        cur = dq.popleft()
        x = cur[0]
        y= cur[1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0<= ny < n and visit[ny][nx]==0 and maps[ny][nx]==1:
                visit[ny][nx]=visit[y][x]+1
                dq.append((nx,ny))

    answer = visit[n-1][m-1]
    if answer==0:
        answer=-1

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))