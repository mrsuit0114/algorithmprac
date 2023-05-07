import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dicA={}
count = 0

for i in range(n):
    name = input().strip()
    dicA[name] = True
for j in range(m):
    name = input().strip()
    if name in dicA :
        count+=1
print(count)

# 딕셔너리에서 value값이 필요한 경우가 아니면 set을 쓰자