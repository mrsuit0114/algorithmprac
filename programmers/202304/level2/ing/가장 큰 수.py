


# 뒷자리 크기별로도 다시 정렬해야함 34 30 3 중에서 34가 먼저나와야하는데
# def solution(numbers):
#     answer = ''
#     numbers = list(map(str,numbers))
#     numbers.sort(key = lambda x :(-int(x[0]), len(x))) #앞자리 오름차순 길이 오름차순

#     for i in numbers:
#         answer+=i

#     return answer

solution([6,10,2])

# print("d">'af') 앞자리부터 차례대로 비교함

# 문자열로 바꾼 배열을 만들고 길이오름차순정렬 후 앞자리만 비교해서 정렬하면될듯
# 앞자리비교해서 같으면 길이 오름차순
# 앞자리 정렬 후 길이 오름차순 차이있나?

# 문제 제대로 읽기
# 숫자가 들어있는 배열로 주니까 앞자리 시작을 기준으로 숫자를 넣을수있는 2차원 배열 생성
# numbers돌면서 앞자리별로 자릿수가 작은 순서대로 --> str변환?, 같다면 둘중 큰수가 앞에 오도록 --> 나눠서 몫이 있는지 확인하는 방식으로
# 앞자리랑 자릿수같은수가 언제나올줄알고 이걸 따로처리해
# 그리고 이 모든 배열을 9부터 돌면서 순서대로 str만들어서 출력

# numbers를 앞자리가 크고 같다면 길이가 짧은순서로 정렬하고 차례대로 이어붙히면 될듯
# 길이로 먼저 정렬하고