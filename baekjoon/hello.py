import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(100000)

#---------------------------------------------

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
visit = [0]*n
m = 1e9

def dfs(depth, start,cost):
    global m
    if depth == n-1 and l[start][0] !=0:
        m = min(m,cost+l[start][0])
        return
    for i in range(n):
        if not visit[i] and l[start][i]!=0:
            visit[i]=1
            dfs(depth+1,i,cost+l[start][i])
            visit[i]=0
visit[0]=1
dfs(0,0,0)
print(m)
#---------------------------------------------
# n = int(input())
# board=[]
# hmax=0

# for i in range(n):
#     a=list(map(int,input().split()))
#     hmax = max(hmax,max(a))
#     board.append(a)

# dx = (1, -1, 0, 0)
# dy = (0, 0, 1, -1)
# cnt = 0

# def dfs(x, y, h):
#     visited[x][y] = True

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > h and not visited[nx][ny]:
#             dfs(nx, ny, h)


# for h in range(hmax):
#     _cnt = 0
#     visited = [[False for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] > h and not visited[i][j]:
#                 dfs(i, j, h)
#                 _cnt += 1
#     cnt = max(cnt, _cnt)

# print(cnt)



#---------------------------------------------

# input = sys.stdin.readline

# n=int(input())

# arr = list(map(int,input().split()))
# arr.sort()
# ans=0

# for i in itertools.permutations(arr,n):
#     res=0
#     for j in range(n-1):
#         res += abs(i[j]-i[j+1])
#     ans = max(ans,res)
# print(ans)

#---------------------------------------------

# arr =[]
# for i in range(9):
#     arr.append(int(input()))
# arr.sort()
# res = sum(arr) -100

# for i in range(9):
#     for j in range(i):
#         if arr[i]+arr[j]==res:
#             arr.remove(arr[i])
#             arr.remove(arr[j])
#             print(*arr,sep='\n')
#             exit(0)
#---------------------------------------------

# n = int(input())
# array=[]
# for i in range(n):
#     array.append(input().strip())

# aset = set(array)
# array = list(aset)
# array.sort()
# array.sort(key=lambda x: len(x))  #오름차순이 기본 내림차순하려면 ,reverse=1

# print(*array,sep='\n')
#---------------------------------------------

# N, r, c = map(int, input().split())

# ans = 0

# while N != 0:

# 	N -= 1

# 	# 1사분면
# 	if r < 2 ** N and c < 2 ** N:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 0

# 	# 2사분면
# 	elif r < 2 ** N and c >= 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 1
# 		c -= ( 2 ** N )
        
# 	# 3사분면    
# 	elif r >= 2 ** N and c < 2 ** N: 
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 2
# 		r -= ( 2 ** N )
        
# 	# 4사분면    
# 	else:
# 		ans += ( 2 ** N ) * ( 2 ** N ) * 3
# 		r -= ( 2 ** N )
# 		c -= ( 2 ** N )
    
# print(ans)


#---------------------------------------------

# ans = 0
# n=int(input())
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
    
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1

#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다.
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)


#---------------------------------------------

# def hanoi(n,start,via,to):
#     if(n==1):
#         print(start,to)
#         return
#     hanoi(n-1,start,to,via)
#     print(start,to)
#     hanoi(n-1,via,start,to)
# n = int(input())
# print(2**n-1)
# if n <=20 : hanoi(n,1,2,3)

#---------------------------------------------

# n = int(input())
# ans =0
# if n<100:
#     ans +=n
# else:
#     ans=99
#     for i in range(100,n+1):
#         stri  = str(i)
#         if int(stri[0])+int(stri[2]) == 2*int(stri[1]):
#             ans+=1

# print(ans)

#---------------------------------------------

# a,b = map(int, input().split())
# n= int(input())

# l=[0,a]  #밑바닥길이
# h=[0,b]  #높이

# for i in range(n):
#     sero, le = map(int,input().split())  #세로로 자르냐
#     if(sero):  #세로로 자르면 밑바닥 길이 영향
#         l.append(le)  #밑바닥 자르는 인덱스
#     else:
#         h.append(le)
# l.sort()
# h.sort()

# lmax=0
# hmax=0

# for i in range(1,len(l)):
#     lmax = max(lmax,l[i]-l[i-1])
# for i in range(1,len(h)):
#     hmax = max(hmax,h[i]-h[i-1])

# if len(l)==1:
#     lmax = a
# if len(h)==1:
#     hmax = b

# print(lmax*hmax)

#0도 넣어서 계산했어야했는데
#안자른 경우의 예외처리가 필요함

#---------------------------------------------

# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우 
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]

# n = int(input())
# for _ in range(n):
#     a = int(input())  #짝수
#     prm = prime_list(a)
#     l=a//2  #짝수만준다
#     r=l
#     while l>0:
#         if l in prm and r in prm:
#             print(l,r)
#             break
#         else:
#             l-=1
#             r+=1

# n = 10000 # 2부터 1,0000까지의 모든 수에 대하여 소수 판별
# array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# # 에라토스테네스의 체 알고리즘 
# for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
#     if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
#         # i를 제외한 i의 모든 배수를 지우기
#         j = 2 
#         while i * j <= n:
#             array[i * j] = False
#             j += 1

# n = int(input())

# for i in range(n):
#     a = int(input())
#     l,r = 2,a
#     tl,tr=2,a
#     while(l<=r):
#         if(array[l] and array[r]): #둘다 소수이면서
#             if(l+r==a):
#                 tl=l
#                 tr=r
#                 l+=1
#             elif(l+r<a):
#                 l+=1
#             else:
#                 r-=1
#         if(not array[l]):
#             l+=1
#         elif(not array[r]):
#             r-=1
#     print(tl,tr)
#---------------------------------------------

# a = int(input())

# for i in range(a):
#     n,s = input().split()
#     n= int(n)
#     for j in s:
#         print(j*n,end="")
#     print("")

# n = int(input())
# for i in range(n):
#     result = ""
#     s = list(input().split())
#     for j in s[1]:
#         result += int(s[0])*j
#     print(result)
#---------------------------------------------


# s = list(sys.stdin.readline().split())  # white space는 무시함
# print(s)

# a = input().strip()
# word = 0  #단어가 주어지지 않는 경우도 넣어야하나보다
# for i in a:
#     if i==' ':
#         word+=1
# if(a):
#     print(word+1)
# else:
#     print(word)
#---------------------------------------------

# a,b = map(int, input().rstrip().split());

# print(a + b,a-b,a*b,a//b,a%b, sep='\n')
#---------------------------------------------

# res = 1
# for i in range(3):
#     a=int(input());
#     res*=a

# res = str(res)

# result= [0 for i in range(10)]  # [0]*10

# for i in res:
#     result[int(i)]+=1
# print(*result,sep='\n')
#---------------------------------------------




