













#시간초과남 어지간한경우아니면 중간에 n^2아닐텐데
#해당부분도 이분탐색으로 해야하나

# import math
# def solution(sequence, k):
#     answer = []
#     endidx = 0
#     # for i in range(len(sequence)-1,-1,-1):
#     #     if sequence[i]<=k: #주어진 수열은 만족하는 경우가 항상 존재
#     #         endidx=i
#     #         break
#     #endidx를 이분탐색으로 구하고 시작해야겠다
#     r = len(sequence)-1
#     l = 0
#     while l<=r:
#         mid = math.floor((r+l)/2)
#         if sequence[mid]>k:
#             r=mid-1
#         else:
#             l=mid+1
#         endidx = mid

#     arr = []
#     tmp = 0
#     for i in range(endidx,-1,-1):
#         arr.insert(0,sequence[i])
#         if sum(arr) > k:
#             arr.pop()
#         elif sum(arr)==k:
#             tmp = i
#             while tmp>0 and sequence[tmp-1]==arr[-1]:
#                 tmp-=1
#             if tmp<0:
#                 answer= [0,len(arr)-1]
#                 return answer
#             answer = [tmp,tmp+len(arr)-1]
#             return answer


#     return answer

# # solution([1, 2, 3, 4, 5], 7)
# solution([1, 1, 1, 2, 3, 4, 5], 5)

# #부분수열의 합이니까 뒤에서부터 탐색해서 k보다 작거나 같은 원소가 나온 순간부터 고려할 것






# # def solution(sequence, k):
# #     answer = []
# #     arr = [sequence[-1]]
# #     tmpidx = 0

# #     if sum(arr)==k: #처음부터 맞는 경우
# #         tmpidx=0
# #         for i in range(len(sequence)-2,-1,-1):
# #             if sequence[i]!=k :
# #                 tmpidx = i+1
# #                 answer = [tmpidx,tmpidx]
# #                 return answer
# #     else:
# #         for i in range(len(sequence)-2,-1,-1):
# #             if sum(arr) + sequence[i] > k :
# #                 arr.pop()
# #                 arr.insert(0,sequence[i])
# #             elif sum(arr)+sequence[i] == k:
# #                 tmpidx = i
# #                 while arr[-1]==sequence[tmpidx] and tmpidx:
# #                     tmpidx-=1
# #                 answer = [tmpidx,tmpidx+len(arr)]
# #                 return answer
# #             else:
# #                 arr.insert(0,sequence[i])

# #     return answer

# #처음부터맞는경우, 충분한 구간동안 동일한원소가 나오는 경우를 고려해야함

# # k = solution([2, 2, 2, 2, 2], 6)
# # print(k)
# # def solution(sequence, k):
# #     answer = []
# #     length = len(sequence)
# #     arr = []
# #     arr.append(sequence[length-1])
# #     if sum(arr)==k:
# #         answer = [length-1,length-1]
# #         return answer

# #     for i in range(length-2,-1,-1):
# #         if sum(arr[:-1])+ sequence[i] > k :
# #             arr.pop()
# #         elif sum(arr[:-1])+ sequence[i] == k :
# #             for j in range(i,-1,-1):
# #                 if sequence[j]!=sequence[i]:
# #                     answer = [j+1,j+len(arr)]
# #                     return answer
# #                 else:
# #                     if j==0:
# #                         answer = [0,len(arr)-1]
# #                         return answer
# #         arr.insert(0,sequence[i])

# #     return answer

# # 끝원소부터 insert(0, a)하고 합이 작으면 계속넣고 크면 pop()하고 넣고
# # 같다면 끝원소랑 비교 같으면 계속 idx앞으로당기고 틀리면 리턴 


# # def solution(sequence, k):
# #     answer = []
# #     arr = [] # 부분 수열
# #     arr.append(sequence[-1])
# #     tempidx = 0
# #     length = len(sequence) #주어진 수열의 길이
# #     for i in range(length-2,-1,-1):
# #         if sum(arr) + sequence[i] > k :
# #             arr.pop()
# #             arr.insert(0,sequence[i])
# #         elif sum(arr) + sequence[i] == k:
# #             arr.insert(0,sequence[i])
# #             for j in range(i-1,-1,-1):
# #                 if sum(arr[:-1]) + sequence[j] == k:
# #                     arr.pop()
# #                     arr.insert(0,sequence[j])
# #                     tempidx = j
# #                 else:
# #                     answer = [j,j+len(arr)-1]
# #                     return answer
# #             answer = [tempidx,tempidx+len(arr)-1]
# #             return answer
            
# #         else :
# #             arr.insert(0,sequence[i])

# #     return []


# #같은 원소도있어서 비내림차순이라는거같은데 그냥 오름차순으로 생각하겠음
# # 짧은 길이의 수열을 찾아야 하기 때문에 뒤에서부터 계산
# #뒤의 원소를 하나씩 더하면서 값을 넘어가면 제일뒤의 원소를 빼고 더하고 만약 일치하면 길이와 현재 idx로 구간
# #가장 먼저 찾는게 길이가 제일 짧지않나
# # 같은길이면서 idx가 더 앞쪽인경우.. 모든원소가 같은경우
# #우선 찾으면 길이를 고정해놓고 제일뒤의원소빼고 더하는게 값이 다르면 바로리턴 같으면 틀릴때까지