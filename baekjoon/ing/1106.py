# import sys

# input = sys.stdin.readline

# n, c = map(int,input().split())
# cities = []

# for i in range(c):
#     a,b = map(int,input().split())
#     city = (a,b)
#     cities.append(city)
# cities.sort(key = lambda x: x[0]/x[1])

# dp = [10e9]*101

# money = 10e9

# for city in cities:
#     if n<city[1]:  #한번에 되는 경우
#         money = min(money, city[0])

# for city in cities:
#     count = 1
#     while city[1]*

C,N = map(int,input().split())
cost_list = [list(map(int,input().split())) for _ in range(N)]
dp = [1e7 for _ in range(C+100)]
dp[0]=0
 
for cost, num_people in cost_list:
    for i in range(num_people,C+100):
        dp[i] = min(dp[i-num_people]+cost,dp[i])
 
print(min(dp[C:]))



