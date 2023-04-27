def solution(s):
    answer = 0
    cnt = 0
    i = 0
    while s:
        w = s[0]
        for i in range(len(s)):
            if s[i] == w:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0 or i == len(s) - 1:
                s = s[i+1:]
                answer += 1
                break
            
    return answer


# 문제를 또 잘못이해햇네
# def solution(s):
#     answer = 0
#     dic = {}
#     idx = 0
#     pivot = ""
#     while idx<len(s):
#         if pivot == "":
#             pivot = s[idx]
#         if s[idx] in dic:
#             dic[s[idx]]+=1
#         else:
#             dic[s[idx]]=1
#         flag=0
#         for j in dic.values():
#             if j==dic[pivot]:
#                 flag+=1
#         if flag==2:
#             dic.clear()
#             answer+=1
#             pivot=""
#         idx+=1
#     if dic:
#         answer+=1



#     return answer
# 왜틀리는거냐
# 문제좀 잘 읽자 처음나오는게 x이고 이거랑 같아지는 경우로 해야하잖아



# 문자열 돌면서 문자나올때마다 dic +=1, set에 value값 넣어서 길이가 다르면 같은 횟수 문자가 있는것 ans+=1, dic.clear

# def solution(s):
#     answer = 0
#     dic = {}
#     s1 = set([])
#     for i in s:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#         for j in dic.values():
#             s1.add(j)
#         if len(s1)!= len(dic) and len(dic)!=1:
#             answer+=1
#             dic.clear()
#         s1.clear()
#     # 마지막문자에서 갯수가 일치해서 끝나는 경우 이건 정상적으로 작동
#     # 마지막문자까지 일치하지않아서 억지로 끝나는 경우 
#     if len(dic)!=0:
#         answer+=1

#     return answer

solution("abracadabra")

# dic으로 해당 문자가 나올때마다 +1 해주고 갯수확인 만약같은문자가 있으면 ans+1하고 dic 초기화

