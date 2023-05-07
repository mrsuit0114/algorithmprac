import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])

# 굳이 dict를 두개를 나눠서 쓸 필요가 없었네
# isdigit

# import sys
# input = sys.stdin.readline

# n, q = map(int,input().split())

# mons_idx = {}
# mons_name = {}

# count = 1

# for i in range(n):
#     name  = input().strip()
#     mons_idx[str(count)] = name
#     mons_name[name] = count
#     count+=1

# for i in range(q):
#     cmd = input().strip()
#     if cmd in mons_idx:
#         print(mons_idx[cmd])
#     elif cmd in mons_name:
#         print(mons_name[cmd])