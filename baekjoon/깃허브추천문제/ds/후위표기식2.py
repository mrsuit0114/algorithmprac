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
        y = stk.pop()
        x = stk.pop()
        if s == "*":
            x *=y
        elif s == "/":
            x /=y
        elif s == "+":
            x +=y
        elif s == "-":
            x -=y
        stk.append(x)
print(format(stk[0],".2f"))
