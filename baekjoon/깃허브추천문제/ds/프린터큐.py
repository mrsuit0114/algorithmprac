from collections import deque
import heapq
import sys

input = sys.stdin.readline

N = int(input())


for i in range(N):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    dq = deque(arr)
    heap = [-x for x in arr]
    heapq.heapify(heap) # 리턴값없고 인자로받은 리스트를 직접변경
    idx = m
    count=0
    while True:
        todel = -heapq.heappop(heap)
        while dq[0]!= todel:
            tmp = dq.popleft()
            dq.append(tmp)
            idx-=1
            if idx<0:
                idx = len(dq)-1
        dq.popleft()
        count+=1
        idx -= 1
        if idx == -1:
            print(count)
            break
        


