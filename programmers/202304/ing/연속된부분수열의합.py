def solution(sequence, k):
    answer = []
    return answer


# def solution(sequence, k):
#     answer = []
#     length = len(sequence)
#     arr = []
#     arr.append(sequence[length-1])
#     if sum(arr)==k:
#         answer = [length-1,length-1]
#         return answer

#     for i in range(length-2,-1,-1):
#         if sum(arr[:-1])+ sequence[i] > k :
#             arr.pop()
#         elif sum(arr[:-1])+ sequence[i] == k :
#             for j in range(i,-1,-1):
#                 if sequence[j]!=sequence[i]:
#                     answer = [j+1,j+len(arr)]
#                     return answer
#                 else:
#                     if j==0:
#                         answer = [0,len(arr)-1]
#                         return answer
#         arr.insert(0,sequence[i])

#     return answer

# 끝원소부터 insert(0, a)하고 합이 작으면 계속넣고 크면 pop()하고 넣고
# 같다면 끝원소랑 비교 같으면 계속 idx앞으로당기고 틀리면 리턴 


# def solution(sequence, k):
#     answer = []
#     arr = [] # 부분 수열
#     arr.append(sequence[-1])
#     tempidx = 0
#     length = len(sequence) #주어진 수열의 길이
#     for i in range(length-2,-1,-1):
#         if sum(arr) + sequence[i] > k :
#             arr.pop()
#             arr.insert(0,sequence[i])
#         elif sum(arr) + sequence[i] == k:
#             arr.insert(0,sequence[i])
#             for j in range(i-1,-1,-1):
#                 if sum(arr[:-1]) + sequence[j] == k:
#                     arr.pop()
#                     arr.insert(0,sequence[j])
#                     tempidx = j
#                 else:
#                     answer = [j,j+len(arr)-1]
#                     return answer
#             answer = [tempidx,tempidx+len(arr)-1]
#             return answer
            
#         else :
#             arr.insert(0,sequence[i])

#     return []

solution([1, 1, 1, 2, 3, 4, 5], 5)

#같은 원소도있어서 비내림차순이라는거같은데 그냥 오름차순으로 생각하겠음
# 짧은 길이의 수열을 찾아야 하기 때문에 뒤에서부터 계산
#뒤의 원소를 하나씩 더하면서 값을 넘어가면 제일뒤의 원소를 빼고 더하고 만약 일치하면 길이와 현재 idx로 구간
#가장 먼저 찾는게 길이가 제일 짧지않나
# 같은길이면서 idx가 더 앞쪽인경우.. 모든원소가 같은경우
#우선 찾으면 길이를 고정해놓고 제일뒤의원소빼고 더하는게 값이 다르면 바로리턴 같으면 틀릴때까지