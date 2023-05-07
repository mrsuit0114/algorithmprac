import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    m = int(input())
    if m!=0:
        heapq.heappush(heap,-m)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
