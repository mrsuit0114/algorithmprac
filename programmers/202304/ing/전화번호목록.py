
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

# len 이 n만큼 들거라 생각해서 안했는데 안그런가봄 아마 파이썬에서 내부에 있어서 그런가
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if len(phone_book[i]) < len(phone_book[i+1]):
#             if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
#                 answer = False
#                 break
#     return answer

# 시간초과
# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)):
#         for j in range(len(phone_book)):
#             if phone_book[i].find(phone_book[j]) == 0:
#                 if i!=j:
#                     answer = False
#     return answer





# 데이터가 1000000개니까 n^2도 힘들지않나?
# 두개를 비교할때 길이가 더 짧아야만 접두어 가능성이있음
# 두개를 비교했을 때 접두어인지 확인하려면 각각 문자를 비교해가면서 일치하는지 확인해봐야지
# 검증은 고정인데 어떤방식을해야 빨리 확인하나?