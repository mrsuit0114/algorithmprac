def solution(stones, k):
    answer = 0
    lp = 0
    rp = k-1
    m = 200000001

    while rp<len(stones)-1:
        tmp = max(stones[lp:rp+1]) # 여러개일때가 문제구나
        if tmp<m:
            m = tmp
        lp = lp+ k-stones[lp:rp+1:-1].index(tmp)
        rp = lp+k-1
        # tmp == m  일때는?
        # tmp 값이 여러개일때는?

    answer = m
    return answer



# def solution(stones, k):
#     answer = 0
#     lp = 0
#     rp = k-1
#     m = 200000001

#     while rp<len(stones)-1:
#         tmp = max(stones[lp:rp+1])
#         if tmp<m:
#             m = tmp
#         lp = lp+stones[lp:rp+1].index(tmp)+1
#         rp = lp+k-1

#     answer = m
#     return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)
# 충분히 작은값이 k개 만큼 있는 구간이 최대 인원을 정한다
#k개씩 구간을 짝지었을때 최댓값이 가장 작은 구간이 문제되는 것? -> 2개실패 시간초과
# 최댓값이 바뀌는 구간만 빠르게 확인하고 넘어가는법 -> 최댓값 idx+1 부터
# 예외처리가 좀 필요해보임
# 모든값이 같을때 진행이안됨