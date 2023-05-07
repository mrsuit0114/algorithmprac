import sys
input = sys.stdin.readline

n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1): # 범위
  if a[i]: #
    primes.append(i)
    for j in range(2*i, n+1, i): # i의 다음번째 수부터 끝까지 i 인터벌로
        a[j] = False

input()
arr = list(map(int,input().split()))

count = 0
for k in arr:
   if a[k]:
      count+=1

print(count)