from collections import deque
import math

def solution(n, stations, w):
    answer = 0
    last = 1 # 전파안받기 시작하는 지점
    dq = deque(stations)
    while last<=n:
        if dq:
            tmp = dq.popleft() # station의 중심
            tmpl = max(0,tmp-w) # station의 영향 최소지점
            tmpr = tmp+w
            answer += math.ceil((tmpl-last)/(2*w+1))
            last = tmpr + 1
        else:
            answer+=math.ceil((n-last+1)/(2*w+1))
            return answer
        
    # if last == n:  while에서 등호붙힌거랑 뭐가 차이가나서 테스트 13결과가 달라지냐?
    #       answer+=1 last==n일 때 dq에서 처리했을 수도 있는데 더하면 달라지네

    return answer

# 다른사람 풀이 난 몫을구해서한거고 풀이는 곱으로해서함 나눗셈보다 곱셈이 빨라서 그런가봄

def solution(n, stations, w):
    ans = 0
    idx = 0
    location = 1

    while(location <= n) :
        if(idx < len(stations) and location >= stations[idx]-w) :
            location = stations[idx]+w+1
            idx += 1
        else :
            location += 2*w+1
            ans += 1
    return ans


print(solution(3,[1,2,3],1))




# 이분탐색인가? 비슷한 문제 봄 아닌거같기도하고?
# station에 따라 구간들이 나뉘어있음
# station의 영향시작지점과 마지막 기지국 영향지점 구간의 몫을 올림하고  
