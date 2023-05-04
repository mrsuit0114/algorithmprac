from collections import deque
import sys

input = sys.stdin.readline

for i in range(int(input())):
    n, t = map(int,input().split())
    docs = list(map(int,input().split()))
    dq = deque(docs)
    count=0
    while True:
        k = max(dq)
        cur = dq.popleft()
        if cur<k:
            dq.append(cur)
            if t==0:
                t=len(dq)-1
            else:
                t-=1
        else:
            count+=1
            if(t==0):
                print(count)
                break
            t-=1


