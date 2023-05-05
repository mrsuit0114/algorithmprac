import sys
input = sys.stdin.readline

for i in range(int(input())):
    stk = 0
    tmp = input().strip()
    for s in tmp:
        if s == "(":
            stk+=1
        else:
            stk-=1
        if stk<0:
            print("NO")
            break
    else :
        print("NO" if stk else "YES")