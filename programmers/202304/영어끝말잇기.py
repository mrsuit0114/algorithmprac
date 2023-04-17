import math

def solution(n, words):
    answer = []
    gamewords = {} #나온 단어들
    lastword =words[0] #마지막에 나온 단어
    gamewords[words[0]]=True


    erridx = 0
    for i in range(1,len(words)):
        if (lastword[-1] != words[i][0]) or (words[i] in gamewords):
            erridx = i
            break
        lastword = words[i]
        gamewords[lastword]=True
    if erridx!=0:
        answer = [erridx%n+1, math.floor(erridx/n)+1]
    else:
        answer = [0,0]

    return answer

# solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
solution(2,['land', 'dream', 'mom', 'mom', 'ror'])

#dictionary사용할듯 규칙에 어긋나는 idx구해서 몇번째사람인지 판단가능