def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

# def solution(answers):
#     answer = []
#     player1 = 0
#     player2 = 0
#     player3 = 0

#     p2sol = [2,1,2,3,2,4,2,5] * (len(answers)//8+1)
#     p3sol = [3,3,1,1,2,2,4,4,5,5] * (len(answers)//10+1)

#     for i in range(1,len(answers)+1):  # 문제번호
#         #1번 수포자
#         if answers[i-1]==i:
#             player1+=1
        
#         #2번 수포자
#         if i%2:
#             if answers[i-1] == 2:
#                 player2+=1
#         else:
#             if answers[i-1] == p2sol[i-1]:
#                 player2+=1
        
#         #3번 수포자
#         if answers[i-1] == p3sol[i-1]:
#             player3 += 1
        
#     k = max(player1,player2,player3)

#     # for i,player in enumerate([player1,player2,player3]):
#     #     if player == k:
#     #         answer.append(i+1)
#     if k == player1:
#         answer.append(1)
#     if k == player2:
#         answer.append(2)
#     if k == player3:
#         answer.append(3)
        
    

#     return answer
#왜 안되는거냐?

solution([1, 3, 2, 4, 2])