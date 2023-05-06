import sys
input = sys.stdin.readline

n = int(input())
exp = input().strip()
arr = []
for i in range(n):
    arr.append(int(input()))

stk = []

for s in exp:
    if "A"<=s and s<="Z":
        stk.append(arr[ord(s)-ord("A")])
    else:
        if s == "*":
            y = stk.pop()
            x = stk.pop()
            x *=y
            stk.append(x)
        elif s == "/":
            y = stk.pop()
            x = stk.pop()
            x /=y
            stk.append(x)
        elif s == "+":
            y = stk.pop()
            x = stk.pop()
            x +=y
            stk.append(x)
        elif s == "-":
            y = stk.pop()
            x = stk.pop()
            x -=y
            stk.append(x)
print(format(stk[0],".2f"))

