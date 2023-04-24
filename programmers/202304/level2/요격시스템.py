def solution(targets):
    answer = 0
    dis = 10e9
    targets.sort(key = lambda x : (x[1], x[0]))
    while targets:
        tmp = targets.pop()
        if dis>= tmp[1] :
            answer+=1
            dis = tmp[0]
        else:
            dis = max(dis,tmp[0])

    return answer

def solution(targets):
    answer = 0
    dis = 10e9 # 이 지점보다 위에있다면 한번에 지워지는 것
    targets.sort(key = lambda x : (x[1], x[0]))
    while targets:
        tmp = targets.pop()
        # 미사일의 끝지점이 dis보다 크면 터짐 만약 작거나 같다면 미사일을 하나 추가하고 dis를 큰값으로 계속 갱신
        if dis>= tmp[1] :
            answer+=1
            dis = tmp[0]
        else:
            dis = max(dis,tmp[0])

    print(answer)

    return answer

solution([[0,4],[5,10],[6,8],[8,9]])
