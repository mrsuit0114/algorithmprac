def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    bp = 0
    for a in A:
        while B[bp]<=a:
            bp+=1
            if bp==len(B):
                return answer
        answer+=1
        bp+=1
        if bp == len(B):
            return answer


    return answer

# print(solution([2,2,2,2],[1,1,1,1]))
print(solution([5,1,3,7],[2,2,6,8]))

# 둘다 오름차순 정렬을하고 각 배열마다 포인터를 사용해서
# A의 원소를 기준으로 b의 값과 비교, b가 작으면 b의 포인터 증가
# B를 기준으로하는게 코드가 더 간결해질 것
