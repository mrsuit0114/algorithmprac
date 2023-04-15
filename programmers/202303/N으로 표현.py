import sys

input = sys.stdin.readline

n,num = map(int,input().split())

mul=[[]]*10
div=[[]]*10
plus=[[]]*10
minus=[[]]*10
add=[[]]*10  # 덧붙히기

mul[1].append(n)
div[1].append(n)
add[1].append(n)
plus[1].append(n)
minus[1].append(n)

ans = -1

def doMul(k,num):  # k번째 연산
    global n
    global ans
    for i in range(len(mul[k-1])):
        a = mul[k-1][i]*n
        mul[k].append(a)
        b = div[k-1][i]*n
        mul[k].append(b)
        c = plus[k-1][i]*n
        mul[k].append(c)
        d = minus[k-1][i]*n
        mul[k].append(d)
        e = add[k-1][i]*n
        mul[k].append(e)
        if num in [a,b,c,d,e]:
            ans=k
            return

def doDiv(k,num):  # k번째 연산
    global n
    global ans
    for i in range(len(div[k-1])):
        a = mul[k-1][i]//n
        div[k].append(a)
        b = div[k-1][i]//n
        div[k].append(b)
        c = plus[k-1][i]//n
        div[k].append(c)
        d = minus[k-1][i]//n
        div[k].append(d)
        e = add[k-1][i]//n
        div[k].append(e)
        if num in [a,b,c,d,e]:
            ans=k
            return

def doPlus(k,num):  # k번째 연산
    global n
    global ans
    for i in range(len(plus[k-1])):
        a = mul[k-1][i]+n
        plus[k].append(a)
        b = div[k-1][i]+n
        plus[k].append(b)
        c = plus[k-1][i]+n
        plus[k].append(c)
        d = minus[k-1][i]+n
        plus[k].append(d)
        e = add[k-1][i]+n
        plus[k].append(e)
        if num in [a,b,c,d,e]:
            ans=k
            return

def doMinus(k,num):  # k번째 연산
    global n
    global ans
    for i in range(len(minus[k-1])):
        a = mul[k-1][i]-n
        minus[k].append(a)
        b = div[k-1][i]-n
        minus[k].append(b)
        c = plus[k-1][i]-n
        minus[k].append(c)
        d = minus[k-1][i]-n
        minus[k].append(d)
        e = add[k-1][i]-n
        minus[k].append(e)
        if num in [a,b,c,d,e]:
            ans = k
            return

def doAdd(k,num):  # k번째 연산
    global n
    global ans
    for i in range(len(add[k-1])):
        a = int(str(mul[k-1][i])+str(n))
        add[k].append(a)
        b = int(str(div[k-1][i])+str(n))
        add[k].append(b)
        c = int(str(plus[k-1][i])+str(n))
        add[k].append(c)
        d = int(str(minus[k-1][i])+str(n))
        add[k].append(d)
        e = int(str(add[k-1][i])+str(n))
        add[k].append(e)
        if num in [a,b,c,d,e]:
            ans=k
            return


        

def sol(k,num):  # k번째 연산, num
    doAdd(k,num)
    doDiv(k,num)
    doMinus(k,num)
    doMul(k,num)
    doPlus(k,num)

for i in range(2,9):
    sol(i,num)
    if ans != -1:
        print(ans)
        exit(0)
# print(ans)  index에러가 나는건 중간에 답이나와서 리턴했기 때문에 답은 잘나오는듯
