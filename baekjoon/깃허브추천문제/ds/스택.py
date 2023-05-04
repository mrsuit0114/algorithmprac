import sys
input = sys.stdin.readline

stk = []

for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push":
        stk.append(cmd[1])
    elif cmd[0]=="pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif cmd[0]=="size":
        print(len(stk))
    elif cmd[0]=='empty':
        print(1 if len(stk)==0 else 0)
    elif cmd[0] == "top":
        print(stk[-1] if stk else -1)
