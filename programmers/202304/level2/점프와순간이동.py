import math

def solution(n):
    ans = 0
    while n!=0:
        if n%2 : 
            n = math.floor(n/2)
            ans+=1
        else:
            n = math.floor(n/2)
    

    return ans


# 0부터 점프와 순간이동의 순서와 점프를하면 얼마나 해야하는지..
# 순간이동의 특성상 홀수의 경우는 마지막이 무조건 점프로끝나게됨
# 홀수인 경우는 해당 수-1의 도달건전지 +1 을 해주어야할것 같음
# 소인수 분해 2^x*3^y*...*k^z
# 홀수일 때까지 2로 다 나눔 홀수이면 -1하고 다시 반복..



# def solution(n):
#     return bin(n).count('1')

