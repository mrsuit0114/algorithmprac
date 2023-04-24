def solution(routes):
    answer = 1
    routes.sort()
    maxout = routes[0][1]
    for route in routes:
        if route[0]>maxout:
            maxout = route[1]
            answer+=1
        else:
            maxout = min(route[1],maxout)


    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

#다른사람 풀이

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer


# s와 비교, s의 진출보다 route의 진입이 작거나 같으면 s의 진출 = min(route[1],s[1])
# s의 진출보다 route의 진입이 크면 answer+=1, s갱신



# 오름차순 정렬하고 maxout 초기화하고 해당값보다 진입이 크면 하나 추가하고 기존의 진출과 비교해서
# 더 작은 값으로 해야함
# 진입이 작으면

# 수직선이 하나의 긴 고속도로이고 중간에서 들어오고 빠져나갈 수 있는 구조

# 진입점 기준으로 오름차순 정렬하고 스택사용해서
# 스택원소의 진출과 차량의 진입을 비교 진출이 더 크면 그냥 넘어감
# 진출이 더 작으면 ans+=1, 최대진출지점 갱신