import math
def retSum(a,b): # a부터 b까지의 합 둘다 포함
    tmp1 = a*(a-1)//2
    tmp2 = b*(b+1)//2

    return tmp2-tmp1


def solution(n):
    answer = 0
    lp = math.floor(n/2)
    rp = lp+1
    while lp!=0 :
        tmp = retSum(lp,rp)
        if tmp == n:
            answer+=1
            lp-=1
        elif tmp<n:
            lp-=1
        else:
            rp-=1

    return answer+1  # n도 포함해야함 -> +1

print(solution(15))

# n/2+1 까지만 확인하면됨
# n/2, n/2+1 투포인터 활용해서 해당 구간의 합이 값보다 작으면 l포인터를 내리고
# 크면 r포인터를 내리고 l이 1이면 종료
# 홀 짝에 따른 포인터 시작

