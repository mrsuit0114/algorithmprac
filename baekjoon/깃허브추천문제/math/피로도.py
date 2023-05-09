import sys
input = sys.stdin.readline

a,b,c,d = map(int,input().split())
tired = 0
times = 0

for i in range(24):
    if tired+a <= d:
        tired+=a
        times+=1
    else:
        tired = max(0,tired-c)

print(times*b)

    



#나머지가 무조건 남게하는 몫을 구하고부터 시작해야겠는데
#근데 이렇게 안해도 최대가 24시간이라 단순히구하는게 더 편하겠다