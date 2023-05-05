import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ls = list(range(1,n+1))
idx = 0
ans = []

for i in range(n):
    idx = (idx+m-1)%len(ls)
    ans.append(str(ls.pop(idx)))

# print("<",end="")
# print(*ans,sep=", ",end="")
# print(">")
print('<', ', '.join(ans)[:], '>', sep='')

# 해당 idx에 있는 원소를 빼는게 느린가? 파이썬은..
# mylist.pop(idx)과 del mylist[idx]의 차이는 해당 값 반환여부 -> del 이 조금 빠르다 
# del a[:2]처럼 범위 지정 삭제가능