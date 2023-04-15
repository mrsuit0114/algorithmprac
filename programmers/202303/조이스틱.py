def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)  # 이게 더 직관적이네
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer


# def solution(name):
#     answer = 0
#     #고쳐야하는 부분의 idx를 다 저장해두고
#     #다음으로 고쳐야하는 곳은 어디인가?
#     n = len(name)
#     fault = {}
#     faultIdx = []
#     for i in range(n):
#         if name[i]!="A":
#             fault[i] = name[i]
#             faultIdx.append(i)
#     #아스키 코드의 차이가 12이하이면 그대로 13이상이면 25-m
#     #현재 위치랑 제일 가까운거 찾는 함수
#     #현재로부터 idx의 차이가 반보다 작으면 차이만큼 else n-m(idx차이)
#     cur = 0  # 현재 위치
    
#     def nextIdx(cur,faultIdx,n):
#         for i in range(n):
#             # abs(cur-i)  #음수일때가문제네 -1이면 25를 의미하는데
#             if (cur+i)%n in faultIdx :
#                 faultIdx.remove(cur+i)
#                 return cur+i
#             elif cur-i > 0 and cur - i in faultIdx :
#                 faultIdx.remove(cur-i)
#                 return cur-i
#             elif cur-i < 0 and n+cur-i in faultIdx :
#                 faultIdx.remove(n+cur-i)
#                 return n+cur-i

#     visit=0
#     m=len(faultIdx)

#     while visit != m:
#         next = nextIdx(cur,faultIdx,n)
#         t = ord(fault[next]) - ord("A")
#         if t>=13:
#             t = 26-t
#         # 바꾸는 처리
#         answer+=t
#         # 위치를 변경하는 처리에서 거꾸로가는 경우를 안넣었네
#         if n//2 < abs(next-cur):
#             answer = answer + n-abs(next-cur)
#         else:
#             answer+=abs(next-cur)
#         cur = next
#         visit+=1

#     print(answer)

#     return answer
solution("BBBAAAAAAAB")

# solution("BBBAAAAAAAB")  이런 경우 방향에 따라서 한번 다시 뒤로 돌아가야 하는 경우가 있구나 이러면 dfs가 낫겠네
