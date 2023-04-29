# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt



import math

def conv(n,k):
    ret = []
    tmp = 0
    while n!=0:
        tmp = n%k
        ret.append(tmp)
        n = n//k
    ret = list(map(str,ret))
    return "".join(reversed(ret))

def isPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    for i in range(3, math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    ret = conv(n,k)
    tmp = ""
    arr = []
    for i in ret:
        if i!='0':
            tmp+=i
        else:
            if tmp!="":
                arr.append(int(tmp))
            tmp = ""
    if tmp:
        arr.append(int(tmp))

    for a in arr:
        if isPrime(a):
            answer+=1

    return answer

solution(437674,3)
# solution(110011,10)
print("")

# 소수인지는 어떻게 판별할것?
# 최대범위가 20자리비트인데 20자리의 1이 소수인지 시간안에 판별할 수 있나?
# 그렇다고 저 수를 에라토스로 만들수도없고
# 0111...111일때 이게 소수인지 어떻게 판단할거야 19개자리나되는데?
# 제곱근까지만 계산하면 위아래로 식이 반전된 형태라 소수인지 판별가능

