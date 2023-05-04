import sys

input = sys.stdin.readline
#---------------------------------------------

if __name__ == "__main__":
    N = int(input())  # 탑의 개수
    top_list = list(map(int, input().split()))  # 탑 리스트
    stack = []
    answer = []

    for i in range(N):
        while stack:
            if stack[-1][1] > top_list[i]:  # 수신 가능한 상황
                answer.append(stack[-1][0] + 1)
                break
            else:
                stack.pop()
        if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
            answer.append(0)
        stack.append([i, top_list[i]])  # 인덱스, 값

    print(" ".join(map(str, answer)))


#---------------------------------------------
# n = int(input())
# sticks=[]
# ans=[]
# highest = 0
# for i in range(n):
#     sticks.append(int(input()))

# for j in range(n-1,-1,-1):
#     if highest<sticks[j]:
#         ans.append(sticks[j])
#         highest = sticks[j]

# print(len(ans))

#---------------------------------------------
# stk = []
# for i in range(int(input())):
#     n = int(input())
#     if n !=0 :
#         stk.append(n)
#     else:
#         stk.pop()
# print(sum(stk))

#---------------------------------------------
# white = 0
# blue =0
# n = int(input())
# paper = [list(map(int,input().split())) for i in range(n)]

# def sol(n,r,c):  #n은 2의 제곱수, r와 c는 각 색종이의 좌 상단의 좌표
#     color = paper[r][c]
#     global white
#     global blue
#     for i in range(n):
#         for j in range(n):
#             if color != paper[r+i][c+j]:  #단색종이가 아니면
#                 sol(n//2,r,c)  #1
#                 sol(n//2,r+n//2,c)  #2
#                 sol(n//2,r,c+n//2)  #3
#                 sol(n//2,r+n//2,c+n//2)  #4
#                 return
#     #여기 오면 단색종이라는 것
#     if color==0:
#         white+=1
#     else:
#         blue+=1

# sol(n,0,0)

# print(white,blue,sep='\n')

#---------------------------------------------

# n = int(input())
# a = list(map(int,input().split()))

# a.sort()

# tl = 0
# tr = n-1  #갱신해나갈 l, r
# l=0
# r=n-1

# sol = sys.maxsize  #용해도

# while(l<r):  #서로 다른 두개
#     if sol!= min(sol,abs(a[l]+a[r])):
#         tl=l
#         tr = r
#         sol = min(sol,abs(a[l]+a[r]))
#     if a[l]+a[r]<0:
#         l+=1
#     else :
#         r-=1
# print(a[tl],a[tr])

#---------------------------------------------

# n,c = map(int,input().split())

# array = []
# for i in range(n):
#     array.append(int(input()))
# array.sort()

# def bi_search(array,start,end):
#     while start<=end:
#         mid = (start+end)//2
#         current = array[0]  #시작점
#         count = 1  #하나 설치

#         for i in range(1,len(array)):
#             if array[i] >= current + mid:
#                 count +=1
#                 current = array[i]
#         if count >= c:
#             global answer
#             start = mid + 1
#             answer = mid
#         else:
#             end = mid - 1


# start = 1
# end = array[-1] - array[0]
# answer = 0

# bi_search(array, start, end)
# print(answer)

# def sol(tmp):
#     target=arr[0]+tmp  #다음에 설치할 최소지점
#     l=0  #lidx
#     r=s-1  #ridx
#     tn = n-1  #남은 공유기 갯수
#     while(tn!=0):
#         while(l<=r):  #tn==0이라는건 이미 다 배치완료
#             if (target>arr[-1]):  #아직 남았는데 다음 target가 최댓값보다 크다면 불가능이므로 False
#                 return False
#             mid = (l+r)//2
#             if arr[mid]<=target:
#                 l=mid+1
#             else:
#                 r = mid-1
#         target = arr[r]
#         tn-=1  #실제 설치하는 순간
#     return True

# s,n=map(int,input().split())
# arr = []
# for i in range(s):
#     arr.append(int(input()))
# arr.sort()

# tmp = 1  #최대거리 갱신예정


# while(sol(tmp)):tmp+=1

# print(tmp)
        
    
#시작점은 고정으로두고 그 이후 tmp값을 더했을때 이 값보다 크면서 가장 가까운 값의 idx를 어떻게 알아야하나? --> 여기서 이분탐색



#---------------------------------------------

# n, m = map(int,input().split())

# trees = list(map(int,input().split()))

# hmax = max(trees)

# l=hmax-m
# r=hmax
# ans = l  #가능한 길이를 저장할 변수 최댓값을위해 갱신예정
# while(l<=r):
#     tmp = 0  #벌목재 길이의 합  m보다 큰지 비교용
#     mid = (l+r)//2
#     for tree in trees:
#         if tree>mid:
#             tmp+=tree-mid
#     if tmp >= m :
#         ans = mid
#         l=mid+1
#     else:
#         r=mid-1

# print(ans)
#---------------------------------------------

# n = int(input())

# arr = list(map(int,input().split()))
# arr.sort()

# m = int(input())
# arr2 = list(map(int,input().split()))

# for i in arr2:
#     flag=0
#     l=0
#     r=n-1
#     while(l<=r):
#         mid = (l+r)//2
#         if arr[mid]== i:
#             flag=1
#             break
#         elif arr[mid]<i:
#             l=mid+1
#         else:
#             r=mid-1
#     print(1 if flag else 0)

