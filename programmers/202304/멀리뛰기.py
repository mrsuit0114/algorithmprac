def solution(n):
    answer = 0
    dp = [0 for i in range(2001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3,2001):
        dp[i] = (dp[i-2]+dp[i-1])%1234567
    answer = dp[n]

    return answer