
from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] != "*":
                if banned_id[i][j] != users[i][j]:
                    return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)

# 뽑아도 백트래킹 말고 검증할 방법이 안떠오름

# from itertools import permutations

# def search(ids,banned):
#     length = len(banned)
#     able = []
#     for id in ids:
#         if len(id)==length:
#             for x,y in zip(id,banned):
#                 if y!="*":
#                     if x!=y:
#                         break
#             else:
#                 able.append(id)
#     return able

# # 해당 밴아이디 한개와 아이디 목록을 비교해서 가능한 아이디 배열을 반환

# def solution(user_id, banned_id):
#     answer = 0
#     able = []

#     for id in banned_id:
#         tmp = search(user_id,id)
#         able.append(tmp)

    

#     return answer

# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])

# 그러면 2차원 배열을 반환하는데 각 배열에서 하나씩 뽑아서 set에 넣고 길이가 만족될때만 ans+=1
# dfs를 써야하나?
