def solution(triangle):
    answer = 0
    dp=[]
    for i in range(len(triangle)):
        dp.append([0]*(i+1))
    
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0]+triangle[1][0]
    dp[1][1] = dp[0][0]+triangle[1][1]

    for i in range(1,len(triangle)):
        dp[i][0] = dp[i-1][0]+triangle[i][0]
        dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
    for i in range(2,len(triangle)):
        #양 끝은 따로
        for j in range(1,i):
            dp[i][j] = max(dp[i-1][j-1]+triangle[i][j],dp[i-1][j]+triangle[i][j])
    

    answer = max(dp[len(triangle)-1])

    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
