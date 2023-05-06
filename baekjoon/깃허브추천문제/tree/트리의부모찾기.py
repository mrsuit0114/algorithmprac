import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

tree = [[] for i in range(n+1)]
arr = [0] * (n+1)
for i in range(n-1):
    x,y = map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
dq = deque([1])
while dq:
    idx = dq.popleft()
    for i in tree[idx]:
        if arr[i] == 0:
            arr[i] = idx
            dq.append(i)
print(*arr[2:],sep="\n")
# 공통부모는 존재할 수 있지만 부모가 둘 이상은 안됨