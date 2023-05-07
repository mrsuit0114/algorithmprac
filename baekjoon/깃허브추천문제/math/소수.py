import sys
input = sys.stdin.readline

n=10000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1): # 범위
  if a[i]: #
    primes.append(i)
    for j in range(2*i, n+1, i): # i의 다음번째 수부터 끝까지 i 인터벌로
        a[j] = False

x = int(input())
y = int(input())

arr = []
for i in range(x,y+1):
   if a[i]:
      arr.append(i)

if arr:
    print(sum(arr))
    print(arr[0])
else:
   print(-1)