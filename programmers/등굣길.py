def solution(m, n, puddles):
    answer = 0
    dp=[]

    for i in range(m):
        dp.append([0]*n)
    
    dp[0][0] = 1  # 1,1

    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                continue
            if [i+1,j+1] in puddles:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]  # 0,0 일때는 안하고싶은데 그거 하나 위해서 if문을 추가?

    answer = dp[m-1][n-1] % 1000000007
    return answer

print(solution(4,3,[[2,2]]))