
# 어차피 초밥의 가짓수만큼 나오는것도아니라 안쓰이지않나?
# 쿠폰은 가장 끝에 생각하면됨
# 일단은 가장 많은 종류를 포함하는 구간을 찾는게 우선
# 이게 합이나 그런거면 모르겠는데 종류라서 해당 종류를 얼마나 갖고있는지를 나타내는 자료구조가 필요함
# 일단 전부 쿠폰포함으로 가정하고

# 시간초과
# import sys
# from collections import Counter
# input = sys.stdin.readline

# n, d, k, c = map(int, input().split())
# sushi=[]
# for i in range(n):
#     sushi.append(int(input()))

# lp = 0
# rp = lp+k-1
# dic = Counter(sushi[lp:rp+1])
# ans = len(dic)
# tmp = ans

# if c not in dic:
#     dic[c]=0

# while lp<n:
#     delsushi = sushi[lp]
#     lp+=1
#     rp+=1
#     if rp==n:  # 처음은 제외하고 이후 1씩 증가할것이므로 문제없음
#         rp = 0
#     addsushi = sushi[rp]
#     if dic[delsushi] == 1:
#         tmp -= 1
#     dic[delsushi]-=1  # 뺐을때 0이면 종류를 하나 빼야지


#     if addsushi in dic:
#         if dic[addsushi]==0:
#             tmp+=1
#         dic[addsushi]+=1
#     else:
#         dic[addsushi]=1
#         tmp+=1

#     if dic[c]==0:
#         ans = max(ans,tmp+1)
#     else:
#         ans = max(ans,tmp)

# print(ans)