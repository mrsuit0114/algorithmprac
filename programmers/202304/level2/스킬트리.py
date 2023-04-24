def solution(skill, skill_trees):
    answer = -1
    dic = {}
    count=0
    for i in range(len(skill)):
        dic[skill[i]] = i
    # for tree in skill_trees:
    #     tolearn = 0
    #     flag = 1
    #     for s in tree:
    #         if s in dic:
    #             if tolearn==dic[s]:
    #                 tolearn+=1
    #             else:
    #                 flag = 0
    #                 break
    #     count+=1 and flag
    
    # 파이썬 for else 구문
    for tree in skill_trees:
        tolearn = 0
        for s in tree:
            if s in dic:
                if tolearn==dic[s]:
                    tolearn+=1
                else:
                    break
        else :
            count+=1
    

    # print(skill.popleft())
    # print(tmp)  얕은복사라 영향받음
    answer=count

    print(answer)
    return answer

solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])

# 지켜야하는 스킬트리를 딕셔너리에 인덱스(우선순위)값으로 넣고
# 스킬트리들을 돌면서 딕션에있으면 현재 배워야하는 인덱스랑비교해서 일치하면 인덱스증가하고
# 다음문자 찾고 불일치하면 바로 넘어가면됨

# !! 문제를 읽어
# 배우다 말수는 있지만 중간부터 배우는건 안된다 건너뛰고 배우는것도안되고



# 위상정렬이겠지?
# 아니여도 될거같기도하고 사실 개념을 잘 몰라서
#일단 큐가 떠오르는걸
# 큐로하려니까 큐안에 뭐가 앞에 있는지 판단이안되는데
# 위상정렬로 미리 만들자니 스킬이 몇개가 있는지도 모르고
# 중복스킬이 안나오니까 알파벳하나마다 인덱스저장한 딕셔너리넣고
# skill을 돌면서 해당문자가 있는지 확인해서 idx비교하자니 중간원소에서 문제될때 비효율적