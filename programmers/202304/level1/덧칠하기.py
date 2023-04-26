def solution(n, m, section):
    answer = 0
    section.sort()
    last = 0
    for s in section:
        if last<s:
            answer+=1
            last = s+m-1 
    return answer

# section을 정렬하고 첫 원소부터 칠하고 마지막 칠해진 값보다 크면서 가장 먼저나오는 값부터 다시
# 칠하고..

