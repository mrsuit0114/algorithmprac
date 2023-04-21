
def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)  # n//base, n%base
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]

def solution(n, t, m, p):
    answer = ''
    length = t*m
    num=0
    while len(answer)<=length:
        answer += convert(num,n)
        num+=1
    tmp =""
    for i in range(p-1,length,m): # 왜 한번더 나오는 경우도있는거야 length자체가 idx초과라 +1해주면안됨
        tmp+=answer[i]

    return tmp


# ABCDEF
# import math
# def solution(n, t, m, p):
#     answer = ''
#     length = t*m #구해두면 p가 몇이든 뽑고나서 생각가능
#     num = 0 #  현재 진행중인 수
#     abc = ["A","B","C","D","E","F"]
#     ans = []
#     while len(answer)<length:
#         tmp = num
#         ans = []
#         rest = 0
#         while tmp>=n:
#             rest = tmp%n
#             tmp = math.floor(tmp/n)
#             ans.insert(0,str(rest))
#         ans.insert(0,str(tmp))
#         answer = answer + "".join(s for s in ans if int(s)<10 else abc[int(s)%10])
#         num+=1

#     todo=""
#     for i in range(p-1,length+1,m):
#         todo+=answer[i]
#         t-=1
#         if t==0:
#             break

#     return answer

print(solution(16,16,2,1))


# 사람수와 본인의 순서 말해야하는 숫자를 알면 몇자까지 구해야하는지 알 수 있고
# 튜브의 순서에 맞는 인덱스만 뽑아서 문자열을 구성하면되겠다
# 십진수를 해당 진법에 맞는 숫자로 바꾸는 방법
# 해당 진법으로 몫이 0일때까지 나누고 나온 몫을 순서를 반대로한 후 맨뒤에 나머지 붙히기
# 파이썬에서 문자열은 불면이라 insert같은 함수는 못쓰네 그럼 append도 안되나?
# 이럴거면 그냥 배열로 쓰겠다