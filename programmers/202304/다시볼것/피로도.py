def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    visited = [0] * N

    def dfs(k,cnt,dungeons):
        nonlocal answer
        nonlocal N

        if cnt > answer:
            answer = cnt
        for j in range(N):
            if k>=dungeons[j][0] and not visited[j]:
                visited[j]=1
                dfs(k-dungeons[j][1], cnt+1,dungeons)
                visited[j] = 0

    dfs(k,0,dungeons)

    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))

# def solution(k, dungeons):
#     answer = -1
#     route = [0 for i in range(len(dungeons))]
#     num = 0
#     length = len(dungeons)
    

#     def back(k,route,depth): #현재 피로도, 방문한 던전배열, 횟수
#         nonlocal num
#         if depth == length:
#             nonlocal answer
#             answer = max(answer,num)
#             num=0
#             return
#         for i in range(length): #탐색할 던전
#             if route[i]==0: # 아직 안갔다면
#                 if k>=dungeons[i][0]: #해당 던전을 갈 수 있는경우
#                     route[i]=1
#                     num+=1
#                     back(k - dungeons[i][1],route,depth+1)
#                     route[i]=0
#                     num-=1
#                 else:
#                     continue
#     back(k,route,0)

#     return answer

print(solution(80,[[80,20],[50,40],[30,10]]))

# 무조건 요구피로도가 높은곳부터 도는게 많이돌 수 있는게 아닐수있는데
# 소모피로도 오름차순 정렬
# 극단적인경우면 안될거같은데 (1000,1) 이러면
# 요구피로도 오름차순
# 던전이 8개밖에없으면 완탐해야지