# def solution(participant, completion):
#     answer = ''

#     # 둘다 dic으로 만들고 숫자를 비교하기 .. 1
#     part={}
#     com={}

#     for s in participant:
#         if s in part:
#             part[s]+=1
#         else:
#             part[s]=1
#     for k in completion:
#         if k in com:
#             com[k]+=1
#         else:
#             com[k]=1

#     for key in part.keys():
#         #동명이인이 없는 경우
#         # 동명이인이 있는경우
#         if key in com.keys():
#             if part[key]-com[key] != 0:
#                 answer = key
#                 break
#         else :
#             answer = key

#     return answer

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])