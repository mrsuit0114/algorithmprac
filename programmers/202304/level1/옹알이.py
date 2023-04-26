def check(s):
    arr = ["aya", "ye", "woo", "ma"]
    idx = 0
    last = ""
    length = len(s)
    if length<2:
        return False
    while(True):
        word2 = s[idx:idx+2]
        word3 = s[idx:idx+3] # idx+3 이 길이 초과하면 알아서 최대 idx로 취해지는군

        if word2 != last and word2 in arr:
            idx+=2
            last = word2
        elif word3 != last and word3 in arr:
            idx+=3
            last = word3
        else:
            return False
        
        if idx==length:
            return True
        
        if idx>length:
            return False

        


def solution(babbling):
    answer = 0
    for bab in babbling:
        if check(bab):
            answer+=1

    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

# 조합의 갯수는 제한이 없다고 생각하고 해당 문자열이 4가지 옹알이의 조합으로
# 이루어져있으며 연속된 조합은 안나온지 확인하는법
# bab을 2개를 먼저확인 가능한지 확인하고 가능하면 다음 idx부터 다시 2확인 반복
# 불가능하면 3을 확인 가능시 다음 idx 2 반복.., 불가능시 False
# 마지막 idx까지하고 idx가 1이 남는 경우는 불가능한 옹알이
# 2가 남았을수는 없고

#다른사람 풀이

def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i: # 연속된 옹알이 없는 경우
                i=i.replace(j,' ') # 서로 분리시키기위한 공백
        if len(i.strip())==0:
            answer +=1
    return answer



