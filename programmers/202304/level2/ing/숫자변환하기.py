def solution(x, y, n):
    answer = 0
    

    return answer

# 자연수를 곱하거나 더하기때문에 n보다 커지면 더이상 볼필요없음
# 1에서 1000까지만해도 3n제곱인데 말이안되지않나?

from collections import deque
def solution(x, y, n):
    dis = [0 for _ in range(y+1)]
    Q = deque()
    Q.append(x)
    if x == y:
        return 0
    while Q:
        nx = Q.popleft()
        for dir in range(3):
            if dir == 0:
                cur_x = nx * 2
            if dir == 1:
                cur_x = nx * 3
            if dir == 2:
                cur_x = nx + n
            if cur_x > y or dis[cur_x]:
                continue
            if cur_x == y:
                return dis[nx] + 1
            Q.append(cur_x)
            dis[cur_x] = dis[nx] + 1
    
    return -1

print(solution(1,1000000,1))