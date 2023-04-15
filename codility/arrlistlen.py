def solution(A):
    idx=0
    length = 1
    while A[idx]!=-1:
        idx = A[idx]
        length+=1
    print(length)
    return length

solution([1,4,-1,3,2])