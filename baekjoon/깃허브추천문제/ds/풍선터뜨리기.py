import sys
input = sys.stdin.readline

n = int(input())
ballons = [(x,y) for x,y in zip(list(map(int,input().split())),range(1,n+1))]
# nums = deque([(int(n), idx+1) for idx, n in enumerate(input().split())])
ans = []
idx = 0

for i in range(n-1):
    ballon = ballons.pop(idx)
    ans.append(ballon[1])
    tmp = ballon[0]

    if 0<tmp:
        idx = (idx+tmp-1)%len(ballons)
    else:
        idx = (idx+tmp)%len(ballons)  # 파이썬에서 음수의 나눗셈..?
    
ans.append(ballons[0][1])

print(*ans)

# 다른사람 풀이

# from collections import deque


# t = int(input())
# nums = deque([(int(n), idx+1) for idx, n in enumerate(input().split())])
# answer = []
# for _ in range(t):
#     cur = nums.popleft()
#     if cur[0] > 0:
#         nums.rotate(-(cur[0]-1))
#     else:
#         nums.rotate(-(cur[0]))
#     answer.append(cur[1])
# print(*answer)

# deque의 rotate, enumerate활용