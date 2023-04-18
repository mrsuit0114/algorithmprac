import collections

def solution(k, tangerine):
    answer = 0
    dic = {}
    # for t in tangerine:
    #     if t in dic:
    #         dic[t]+=1
    #     else:
    #         dic[t]=1
    dic = collections.Counter(tangerine)
    
    dl = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    dl = dict(dl)

    count = 0
    for g in dl.values():
        count+=g
        answer+=1
        if count >=k:
            break


    return answer

solution(6,	[1, 3, 2, 5, 4, 5, 2, 3])