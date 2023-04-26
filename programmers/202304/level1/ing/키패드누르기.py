def solution(numbers, hand):
    answer = ''
    return answer

#코드가 너무 긴데
# def solution(numbers, hand):
#     answer = ''
#     l=7
#     r=9
#     for i in numbers:
#         if i in [1,4,7]:
#             answer+="L"
#             l = i
#         elif i in [3,6,9]:
#             answer+="R"
#             r = i
#         elif i in [2,5,8]:
#             if abs(i-l)==abs(i-r):
#                 answer += "L" and hand=="left" + "R" and hand=="right"
#                 # answer= answer+ "L" if hand=="left" else "R"
#                 l= hand=="left" and i
#                 r = hand=="right" and i
#             elif abs(i-l)<abs(i-r):
#                 answer +="L"
#                 l=i
#             else:
#                 answer+="R"
#                 r=i
#         else: # 0
#             answer += 
#     return answer