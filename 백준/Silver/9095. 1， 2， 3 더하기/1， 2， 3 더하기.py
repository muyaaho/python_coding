t = int(input())
for x in range(t):
    n = int(input())
    dp = [1,2,4]
    for i in range(3, n):
        dp.append(dp[i-3]+dp[i-2]+dp[i-1])
    print(dp[n-1])