
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# def solution(n, lost, reserve):
#     answer = 0
#     lost.sort()
#     reserve.sort()
#     for i in reserve:
#         if i in lost :  #도난당했지만 여벌이있는사람
#             lost.remove(i)  #그냥 그대로 빼주기
#             reserve.remove(i)
#             continue
#         for j in range(max(1,i-1),i+2): # 앞을 먼저 고려하고 뒤를 주면안되나?
#             if lost.count(j) == 1:
#                 lost.remove(j)
#                 break
#     answer = n- len(lost)

#     return answer
# 대체 어떤 상황에서 안되는거냐?
#9줄에서 3개의 후보를 해놨기 때문에 문제가 있을수있다고 생각해서 바꿨더니 더틀리네?
#앞에서 본인은 뺐는데 왜 틀리는거냐? 오히려 있으면 문제일수 있는거아님?
#자세한 상황은 모르겠네 이미있는사람을 앞에서 빼주면 없는것처럼 판단해서 빌려줄 수 있구나

# 예시의 정렬이 되어있는 상황을 믿지마라
# 예외상황은 반드시 검사하기


print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))
