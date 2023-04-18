import math

def nextnum(k):
    if k%2 :
        return math.floor(k/2)+1
    else:
        return math.floor(k/2)

def solution(n,a,b):
    answer = 1
    s = min(a,b)
    t = max(a,b)

    while s+1!=t or s%2==0 : #인접하고 s가 홀수인경우 루프 탈출
        s = nextnum(s)
        t = nextnum(t)
        answer+=1
#or을 and로했었네

#     return answer

solution(8,4,5)

# 이기는 상황에서 짝수는 2로나눈 몫만큼 홀수는 2로나눈 몫+1을 받는다
# 두 숫자가 서로 인접하고 작은수가 홀수일 경우 만난다
# n은 의미있나?