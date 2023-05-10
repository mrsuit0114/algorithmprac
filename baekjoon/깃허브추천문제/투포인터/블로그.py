import sys
input = sys.stdin.readline

days, n = map(int,input().split())
arr = list(map(int,input().split()))

lp = 0
rp = lp+n-1

tmp = sum(arr[lp:rp+1])
ans = tmp
count = 1

while rp<days-1:
    tmp -= arr[lp]
    lp+=1
    rp+=1
    tmp += arr[rp]
    if ans == tmp:
        count+=1
    elif ans<tmp:
        ans = tmp
        count=1


print(f"{ans}\n{count}" if ans else "SAD")
