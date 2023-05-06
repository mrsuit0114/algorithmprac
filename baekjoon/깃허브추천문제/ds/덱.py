import sys
from collections import deque
input = sys.stdin.readline

dq = deque([])

for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push_front":
        dq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        dq.append(cmd[1])
    elif cmd[0]=="pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0]=="pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0]=="size":
        print(len(dq))
    elif cmd[0]=='empty':
        print(1 if len(dq)==0 else 0)
    elif cmd[0] == "back":
        print(dq[-1] if dq else -1)
    elif cmd[0] == "front":
        print(dq[0] if dq else -1)
    
