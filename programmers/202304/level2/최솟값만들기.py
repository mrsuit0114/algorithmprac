def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=1)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer


solution([1,4,2],[5,4,4])
#정렬해서 큰원소랑 작은원소랑 짝맞춰서 곱한게 최솟값이 아닌경우가 있나?

#return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
#zip 활용하는법도있음