import sys
input = sys.stdin.readline

num, n = input().split()
n = int(n)

print(int(num,n))

# dic = {}
# count = 10
# for i in range(26):
#     tmp = ord("A")+i
#     dic[chr(tmp)] = count
#     count+=1

# ans = 0

# exp = 0
# for k in reversed(num):
#     if k in dic:
#         ans += dic[k]*n**exp
#     else:
#         ans += int(k)*n**exp
#     exp+=1

# print(ans)

