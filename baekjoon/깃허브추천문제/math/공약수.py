from math import gcd
import sys

input = sys.stdin.readline

n=int(input())
if n==2:
    a,b=map(int,input().split())
    g=gcd(a,b)
else:
    a,b,c=map(int,input().split())
    g=gcd(a,b,c)

nums = set()

for i in range(1,int(g**0.5)+1):
    if g%i==0:
        nums.add(i)
        nums.add(g//i)
print(*sorted(nums),end="\n")