a=input().replace("XXXX","AAAA").replace("XX","BB")
print(-1 if 'X' in a else a)


# import sys
# input = sys.stdin.readline

# ret = input().strip()
# tmp = ret.split('.')

# ans = []

# for s in tmp:
#     if s:  # 공백이 아님
#         if len(s)%2:
#             print(-1)
#             exit(0)
#         else:
#             if len(s)//4:
#                 ans += ["AAAA"]*(len(s)//4)
#                 if len(s)%4:
#                     ans+=["BB"]
#             else:
#                 ans+=["BB"]

# idx = 0

# i = 0
# while i<len(ret):
#     if ret[i]==".":
#         print(".",end="")
#     else:
#         print(ans[idx],end="")
#         i+= len(ans[idx])
#         idx+=1
#         continue
#     i+=1