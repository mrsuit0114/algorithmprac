def solution(n, s):
    answer = []
    share = s//n
    if share==0:
        return [-1]
    remain = s%n
    answer = [share]*n
    for i in range(remain):
        answer[-1-i]+=1

    return answer


# 분포가 제일 고른게 곱이 최대라고 보통알고있으니 이렇게 해봄

# 일단 s를 n으로 나눈 몫을 하나씩 나눠갖고 나머지를 나눠가지면 될듯?
