def solution(s):
    answer = ''
    arr = s.split()
    # 숫자로 변경한 배열을 따로 만들어야하나 map사용
    arr_int = list(map(int,arr))
    arr_int.sort()
    answer = str(arr_int[0])+ " " + str(arr_int[-1])
    return answer

solution("-1 -2 -3 -4")

# def solution(s):
#     s = list(map(int,s.split()))
#     return str(min(s)) + " " + str(max(s))
#굳이 정렬할필요없긴했다