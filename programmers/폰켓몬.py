def solution(nums):
    answer = 0
    mons ={}
    for i in nums:
        if i in mons:
            mons[i]+=1
        else :
            mons[i]=1

    num = len(nums)//2
    k = len(mons.keys())

    if k>num:
        answer=num
    else:
        answer=k
    

    return answer

# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))