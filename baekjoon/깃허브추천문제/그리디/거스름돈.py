import sys
input = sys.stdin.readline

money = int(input())

val = money%5
ans = money//5

if money in [1,3]:
    print(-1)
    exit(0)

if val%2==0:
    ans+= val//2
else:
    ans = ans + (val+5)//2-1
    
print(ans)


# dp도가능