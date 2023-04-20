def solution(elements):
    answer = 0
    myset= set()
    for s in range(1,len(elements)+1): #수열의 길이
        for j in range(len(elements)): #수열의 시작idx
            if j+s<len(elements):
                tmp = sum(elements[j:j+s])
            else:
                tmp = sum(elements)-sum(elements[(j+s)%len(elements):j])
            myset.add(tmp)
    answer =len(myset)
    return answer



#중복이없어야한다 -> set, Dic
