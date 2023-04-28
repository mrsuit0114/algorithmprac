# from fractions import gcd

def gcd(a,b):
    while b:
        a,b =b,a%b  # 동시에 안할거면 tmp써야해
    return a

def solution(arr):
    answer = 1
    if len(arr)==1:
        return arr[0]
    arr.sort()
    g = arr[0]
    for i in range(1,len(arr)):
        g = g*arr[i]//gcd(g,arr[i])
    answer = g
    return answer

solution([2,6,8,14])

# 유클리드 호제법
# x%y=r 에서 x와 y의 최대공약수는 y%r의 최대공약수와 같다는 걸 재귀적으로 사용하다가 y%r = 0인 순간 r이 최대공약수
# 최소공배수는 두 수를 곱해서 최대공약수로 나누는 것
# 2개 이상일 때는 어떻게 적용해야 하는가
# 연쇄적으로 최대공약수구하고 모든수를 곱하고 최대공약수로 나눠주면 될 거같음 -> 안됨
# 최소공배수.. 작은값부터 최소공배수 구하고 이 수와 다음수의 최소공배수... 반복

# i행까지 최댓값인 루트를 탔을 때 i+1행까지 최댓값인 루트가 겹치지 않을수도있음
# dp 써야하나 i+2를 구하기위해서 i+1과 i를 참고해야함
# i+1에서는 이전 열만 빼면 최댓값을 취하면되지만 i에서는 arr[i]와 arr[i+1]에서 값을 참고해서 밟아야함



