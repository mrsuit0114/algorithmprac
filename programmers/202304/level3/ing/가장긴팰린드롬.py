def ispal(s):  #무조건 홀수만 오도록 해줄것
    lp =0
    rp = len(s)-1
    while lp!=rp:
        if s[lp]!=s[rp]:
            return False
        lp+=1
        rp-=1
    return True


def solution(s):
    answer = 1
    lp = 1
    rp = len(s)
    while lp<rp: # 등호에서무한루프가 생기는데 만약 rp에서 가장 긴 팰린드롬이면 lp가 rp보다 1작을때 mid==rp, lp가 rp보다 2작을때
        mid = (lp+rp)//2 # mid가 짝수면?
        if mid%2==0:
            mid+=1
        st = 0
        flag = 0
        while st+mid<=len(s):
            if ispal(s[st:st+mid]):
                answer = mid
                flag = 1
                break
            else:
                st +=1
        if flag: # mid길이에 맞는 pal이 존재하는 경우
            lp = mid
        else: # 존재하지 않는 경우
            rp = mid

    return answer

solution("abacde")

# 양끝에서 부터 투포인터 사용해서
# 두개가 서로 다르면 어떻게 이동하지?
# 무조건 홀수여야함 중앙을 기준으로 대칭을 따지기 때문에

