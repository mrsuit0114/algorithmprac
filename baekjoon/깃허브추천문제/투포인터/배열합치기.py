import sys

input = sys.stdin.readline

a,b = map(int,input().split())

ap = 0
bp = 0

Aarr = list(map(int,input().split()))
Barr = list(map(int,input().split()))
ans = []

while ap<a and bp<b:
    if Aarr[ap] > Barr[bp]:
        ans.append(Barr[bp])
        bp+=1
    elif Aarr[ap] < Barr[bp]:
        ans.append(Aarr[ap])
        ap+=1
    else:
        ans.append(Aarr[ap])
        ans.append(Barr[bp])
        ap+=1
        bp+=1

# 둘중 하나가 길이보다 짧은게 있을것 둘다 0일수도있겠네

ans += Aarr[ap:]
ans += Barr[bp:]

print(*ans)

# import sys

# input = sys.stdin.readline

# a,b = map(int,input().split())

# Aarr = list(map(int,input().split()))
# Barr = list(map(int,input().split()))

# ans = sorted(Aarr+Barr)
# print(*ans)

 

